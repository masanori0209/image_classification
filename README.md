# image_classification
CIFAR-10を利用したAIモデルのAPIとSPA＋APIサーバーの構築

## 立ち上げ方

```
docker-compose run front npm install
docker-compose up -d
```

## URL

http://localhost:8080

## 内容

- フロントエンドの方から画像をアップロード
- 内容をmysqlに格納しつつ、imageフォルダに格納
- 外部API（bottle）を呼び出しAIモデルを使って分類（CIFAR-10)し、リクエストを返す
- UIとしてログをテーブルとして表示するようなサービス

## エラーとなる場合

1. 拡張子が画像でないもの
2. 画像データでないもの

## 画像データ

test_dataに格納

## 構成

| サーバー名       | 名称 | ポート番号 |
|:-----|:-------------------------------|:-----|
| Front開発サーバー(Vue.js)    | front | 8080 |
| APIサーバー(Django)    | back | 8000 |
| モックAPIサーバー(bottle)    | ai | 9000 |
| DBサーバー(MySQL)    | db | 3336 |
