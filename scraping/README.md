# scraping

- ダーツライブテーマの URL を`json server`へ登録する

- セットアップ

```
$ pip install -r requirements.txt
```

# How to use

### 1. 環境変数を登録する

```
$ export DARTSLIVE_USER=<ID>
$ export DARTSLIVE_PASS=<PASS>

```

### 2. `define/common_define.py`の`START_USER_LIST`へ任意のユーザ ID を設定する。

- ユーザープロフィールページの URL `https://card.dartslive.com/t/profile/index.jsp?u=XXXXX` の `XXXXX`部分

### 3. プログラムを実行する

- ユーザープロフィールの友達リストから、ユーザーを検索
- 検索したユーザーのテーマの個別情報を取得し、DB へ登録する

```
$ python get_themes.py
```
