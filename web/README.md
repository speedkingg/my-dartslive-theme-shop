# UI ( Web )

# Local version

## 前提

- 対象の`json server`が`http://localhost:3000`で起動していること

## 起動手順

1. `config/config.js` の `ENV` の値を `local`にする
1. `$ yarn install` (初回のみ)`
1. `$ yarn run serve`

# Firebase version

## 前提

- `firebase` で本プロジェクト用アプリを作成している

## 準備

1. `firebase`の`Authentication`で、ログイン プロバイダ：`メール / パスワード`を許可する
   - ユーザを作成しておく（ログインに使用する）
2. `Realtime Database`の設定とデータのインポートを行う

   - `Realtime Database`の rule を設定する（DB は自動で作成される）
     - `$ firebase deploy --only database`
   - [FIrebase コンソール](https://console.firebase.google.com/)から`Database`->`Realtime Database`を選択し、`︙`から`JSONをインポート`で local の`db/db.json`をアップロードする。

3. `firebase`の`Storage`直下に`/dartslive_theme`を作成し、`src/assets/img`配下の画像をアップロードする

## 起動手順

1. `config/config.js` の `ENV` の値を `firebae`にする
2. Firebase コンソールより、ウェブアプリ用の設定スニペットを入手する
3. `config/config.js` の `firebase` の値へ貼りける

```josn:
    firebase:{
        apiKey: "",
        authDomain: "",
        databaseURL: "",
        projectId: "",
        storageBucket: "",
        messagingSenderId: "",
        appId: ""
      }
```

### Firebase 版 Local 起動

4. `$ yarn install` (初回のみ)
5. `$ yarn run serve`

### Firebase 版 Firebase 上で起動

4. ビルドする
   - `$ yarn run build;`
5. （動作確認）
   - `firebase emulators:start --only hosting`
6. Firebase へデプロイ
   - `firebase deploy --only hosting`
7. 表示された URL へアクセス
