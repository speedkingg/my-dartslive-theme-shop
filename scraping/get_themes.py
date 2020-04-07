# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
from urllib.parse import urljoin
from copy import deepcopy

from utils.dartslive_utils import dartslive_utils
from define.common_define import Common_Define
from config.db_config import Db_Config


# メールアドレスとパスワードの指定
USER = os.environ.get("DARTSLIVE_USER")
PASS = os.environ.get("DARTSLIVE_PASS")

try:
    DARTSLIVE_UTILS = dartslive_utils()
except requests.exceptions.ConnectionError as e:
    print("json serverが起動していません。")
    print(e)
    sys.exit(1)

if __name__ == '__main__':

    if(USER is None):
        raise EnvironmentError("環境変数が登録されていません： DARTSLIVE_USER")

    if(PASS is None):
        raise EnvironmentError("環境変数が登録されていません： DARTSLIVE_PASS")

    # セッションを開始
    session = requests.session()

    # ログイン
    login_info = {"id": USER, "ps": PASS}
    login_url = "https://card.dartslive.com/entry/login/doLogin.jsp"
    res = session.post(login_url, data=login_info)
    res.raise_for_status()  # エラーならここで例外を発生させる

    start_user = Common_Define.START_USER_LIST
    img_save_path = "../web/public/img/"

    current_user = DARTSLIVE_UTILS.get_theme_by_user_list(
        session,
        deepcopy(start_user),
        img_save_path
    )

    i = 0
    # 友達の友達を探しに行く
    while i <= Common_Define.ADDITIONAL_SEARCH_HIERARCY_DEPTH:
        updated_user = DARTSLIVE_UTILS.get_theme_by_user_list(
            session,
            deepcopy(current_user),
            img_save_path
        )

        if len(updated_user) == len(current_user):
            print("breaked")
            break

        current_user = deepcopy(updated_user)

        i += 1

    print("get_user_id_from_their_friend_list complete!")
