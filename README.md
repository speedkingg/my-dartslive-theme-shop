# dartslive_theme_list

ショップ以外からダーツライブテーマを購入できるようにする

# Functions： 機能

- ログイン認証 / テーマ閲覧

<img src="https://user-images.githubusercontent.com/26742929/75689922-5c0f6380-5ce5-11ea-81f3-b1621d6c11f2.jpg" width="300"> <img src="https://user-images.githubusercontent.com/26742929/75690055-96790080-5ce5-11ea-9586-5137b4e3c8a8.jpg" width="300">

- 検索 / お気に入り

<img src="https://user-images.githubusercontent.com/26742929/75690064-98db5a80-5ce5-11ea-971a-ffb5840470fc.jpg" width="300"> <img src="https://user-images.githubusercontent.com/26742929/75690072-9973f100-5ce5-11ea-976d-a46c4523d80a.jpg" width="300">

# How to use： 使い方

- 動作環境

```
$ python --version
  Python 3.7.1
$ npm --version
  6.4.1
$ firebase --version
  7.12.1
```

### 1. データを登録する DB をインストール＆起動する

- [`db/README.md`](db/README.md)に準じる

### 2. ダーツライブテーマを収集する

- [`scraping/README.md`](scraping/README.md)に準じる

### 3. web でテーマ情報を閲覧する

- [`web/README.md`](web/README.md)に準じる
  - `2` が収集中でも閲覧できます。
