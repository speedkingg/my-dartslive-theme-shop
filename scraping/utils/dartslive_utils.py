# -*- coding: utf-8 -*-

import re
import json
import requests
from urllib.parse import urljoin

from utils.soup_utils import soup_utils

from config.dartslive_config import Dartslive_Config
from config.db_config import Db_Config


class dartslive_utils:
    def __init__(self):
        self.SOUP_UTILS = soup_utils()
        # テーマ一覧を取得
        # （DBをキャッシュしてテーマの重複をプログラム側で判断する）
        response_theme = requests.get(Db_Config.DB_THEME)
        self.theme_list_by_db = []
        for item in json.loads(response_theme.text):
            self.theme_list_by_db.append(item['id'])

    def get_theme_by_user_list(self, session, user_list, img_save_path):
        """
        user_list -> friend_list
        ユーザーリストのユーザーの友達をDBへ登録する

        Parameters
        ----------
        session: Object link
            DartsLiveにログインした状態のセッション（参照渡し）

        current_user_list : deepcopy(array)
            すでに把握しているダーツライブユーザーページのリストの値渡し

        img_save_path : String
            テーマの画像を保存するパス
        """

        for user_id in user_list:
            # ユーザ一覧ページURL取得
            souped_html = self.SOUP_UTILS.get_souped_html(
                session, Dartslive_Config.BASE_USER_URL + str(user_id))

            user_relative_link = souped_html.select_one(".friend > a")

            # プレイデータを公開していません。に対応
            if user_relative_link is None:
                continue

            user_link = urljoin(Dartslive_Config.BASE_URL,
                                user_relative_link.get("href"))

            # ユーザ一覧ページへ遷移
            souped_html = self.SOUP_UTILS.get_souped_html(session, user_link)
            friend_link_list = souped_html.select(".player > a")

            for friend_link in friend_link_list:

                new_id = friend_link.get("href").replace("index.jsp?u=", "")

                # 共通の友人の場合、処理をスキップする（すでに登録されているため）
                if new_id in user_list:
                    continue

                user_list.append(new_id)
                self.get_theme_by_user_id(
                    session, new_id, img_save_path)

        return 0

    def get_theme_by_user_id(self, session, user_id, img_save_path):
        """
        指定したユーザIDのお気に入りテーマ情報を取得しDBへ保存

        Parameters
        ----------
        session: Object link
            DartsLiveにログインした状態のセッション（参照渡し）

        user_id : String
            ダーツライブユーザーのId

        img_save_path : String
            テーマの画像を保存するパス

        """

        favorite_theme_link = Dartslive_Config.BASE_FAVORITE_URL + user_id

        # お気に入りテーマ一覧取得
        souped_html = self.SOUP_UTILS.get_souped_html(
            session, favorite_theme_link)

        theme_list = souped_html.select(".player > a")

        if len(theme_list) == 0:
            # お気に入りテーマなしの場合
            return 0

        for theme in theme_list:

            img_name = theme.select_one(".themeName").get_text()
            # ファイル使用禁止文字を置換
            fixed_img_name = re.sub(
                '[\\\\|/|:|\\*|?|\”|<|>|\\| ]', '-', img_name)
            img_file_name = fixed_img_name + ".png"

            if fixed_img_name in self.theme_list_by_db:
                continue  # すでに登録されている場合
            else:
                self.theme_list_by_db.append(fixed_img_name)

            themes = {}
            themes["id"] = fixed_img_name
            themes["theme_name"] = img_name
            themes["img_file_name"] = img_file_name
            themes["user_id"] = user_id

            can_buy = theme.select_one(".buy").get_text() == "購入する"
            themes["can_buy"] = can_buy

            if can_buy:
                themes["price"] = theme.select_one(".price").get_text()
            else:
                continue  # 買えないものは登録しない

            r = requests.post(Db_Config.DB_THEME, data=themes)

            if r.status_code == 201:
                # 画像ファイルをダウンロード
                img_url = urljoin(Dartslive_Config.BASE_URL,
                                  theme.select_one("img").get("src"))
                img = requests.get(img_url).content
                with open(img_save_path + img_file_name, "wb") as f:
                    f.write(img)

        return 0
