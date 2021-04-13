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

フロントエンドの方から画像をアップロードし、
その内容をmysqlに格納しつつ、
ログをテーブルとして表示するようなサービス

モックアップ：決められた形式リクエストを返すような形

AI：AIモデルを使って分類し、リクエストを返すような形(CIFAR-10)

エラーとなる場合：

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
