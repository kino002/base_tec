# socket クライアント作成(日本語を送受信する)

import socket

IPaddress = "127.0.0.1" # ローカルホスト
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーを指定
    s.connect((IPaddress, PORT)) # サーバーのアドレスに接続する
    # サーバーにメッセージを送る
    data = "hello2".encode() # 日本語をunicode型に変更
    s.sendall(data) # ソケットにデータを送信します。バイトで指定
    # ネットワークのバッファサイズは1024 サーバーからの文字を取得する
    data2 = s.recv(1024) # ソケットからデータを受信し、結果を bytes オブジェクトで返します。
                        # 一度に受信するデータは、最大でも bufsize=(1024) で指定した量です。
    data2 = data2.decode() # unicode型をstr型に戻す
    print(data2)