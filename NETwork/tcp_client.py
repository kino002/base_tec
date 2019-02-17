# socket クライアント作成

import socket

IPaddress = "127.0.0.1" # サーバー側のIPアドレス
PORT = 50000    # サーバーと同じポート番号

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーを指定
    s.connect((IPaddress, PORT)) # サーバーのアドレスに接続する
    # サーバーにメッセージを送る
    s.sendall(b"hello") # ソケットにデータを送信します。バイトで指定
    # ネットワークのバッファサイズは1024 サーバーからの文字を取得する
    data = s.recv(1024) # ソケットからデータを受信し、結果を bytes オブジェクトで返します。
                        # 一度に受信するデータは、最大でも bufsize=(1024) で指定した量です。
    print(data)