import socket

IPaddress = "127.0.0.1"
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((IPaddress, PORT))   # bind()でsとアドレス、ポートを関係付ける
    print("UDPサーバー起動中")
    while True:
        data, addr = s.recvfrom(1024) # ソケットからデータを受信し、結果を(bytes, address)として返す
        print("data: {}, addr: {}".format(data, addr))