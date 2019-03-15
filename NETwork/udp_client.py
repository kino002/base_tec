import socket

IPaddress = "127.0.0.1"
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # s.sendto(b'hello udp', (IPaddress, PORT))
    s.connect((IPaddress, PORT))    # サーバーのアドレスに接続する
    s.sendall(b"Hello UDP")   # ソケットにデータを送信します。バイトで指定

    s.close()       # 接続を中止