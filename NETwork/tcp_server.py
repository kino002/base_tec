# socket サーバーを作成
import socket

IPaddress = "127.0.0.1" # サーバー側のIPアドレス
PORT = 50000    # ポート番号は、ダイナミック/プライベートポート番号（49152番～65535番）から選ぶ

# AF = IPv4という意味
# TCP/IPの場合は、SOCK_STREAMを使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind((IPaddress, PORT))    # bind()でsとアドレス、ポートを関係付ける
    s.listen(1) # サーバーを有効にして、接続を受け付けるようにします。
                # システムが新しい接続を拒否するまでに許可する未受付の接続の数を指定します。
                # 指定しない場合、デフォルトの妥当な値が選択されます。
                # TCPの場合１対１の通信なので1を指定
    print("TCPサーバー起動中")        
    # connectionするまで待つ
    while True:
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn, addr = s.accept() # 接続を受け付けます。
                                # ソケットはアドレスにbind済みで、listen中である必要があります。
                                # 戻り値は (conn, address) のペアで、 
                                # conn は接続を通じてデータの送受信を行うための 新しい ソケットオブジェクト、 
                                # address は接続先でソケットにbindしているアドレスを示します。
        # データを受け取る
        data = conn.recv(1024)  # ソケットからデータを受信し、結果を bytes オブジェクトで返します。
                                # 一度に受信するデータは、最大でも bufsize=(1024) で指定した量です。
        print("data : {}, addr: {}".format(data, addr))
        # クライアントにデータを返す(b -> byteでないといけない)
        conn.sendall(b"Received: " + data)  # クライアントにdataが送られてきたことを、返す 
                                            # ソケットにデータを送信します。
                                            # ソケットはリモートソケットに接続済みでなければなりません。