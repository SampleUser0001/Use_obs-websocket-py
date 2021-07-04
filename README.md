# Use_obs-websocket-py

OBSのWebsocket、obs-websocket-pyを使ってみる。

## 使い方

### OBS側の準備

1. OBSインストール
2. obs-websocketをインストールする。
   - 下記からインストーラをダウンロード
   - [https://github.com/Palakis/obs-websocket/releases](https://github.com/Palakis/obs-websocket/releases)
3. OBS起動 -> ツール -> Websocket サーバ設定をクリック
4. Websocketの設定を行い、OKボタンを押下。
   - 「WebSockets サーバーを有効にする」をチェック
   - サーバーポートの値を確認
   - 「認証を有効にする」をチェック
   - パスワードに任意の値を入力

### コンテナ起動

1. コンテナ内から見たホストのIPを確認する。
``` sh
ip route | awk 'NR==1 {print $3}'
```
2. sample.envをコピーして、.envファイルを作成
3. .envファイルにコメントに記載してある値を入力して保存。
4. 下記実行。
``` sh
docker-compose up
```

## 参考

- [obs-websocket-pyの使い方ほか:Mokerの徒然日記2.0](https://mokerdiary.hatenablog.com/entry/2019/09/03/000000)

