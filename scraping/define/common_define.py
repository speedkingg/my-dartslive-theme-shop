
# -*- coding: utf-8 -*-


class Common_Define:
    def __init__(self):
        pass

    # 追加で調査する友達リストの深さ（１なら友達の友達まで）
    # ここを増やすと、鬼のように時間がかかるから、原則変更しない
    # （平均友達数を100とすると、100倍かかる時間が増える）
    ADDITIONAL_SEARCH_HIERARCY_DEPTH = 1

    # 最初に友達リストを見るユーザーID
    # 基本的に １IDでよい
    # あまりに検索結果がすくない場合はユーザーの変更を推奨する
    START_USER_LIST = [2172269225196642]
