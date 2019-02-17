"""
ラズパイで、I2C機器をマスター制御する場合は、
sudo aspt-get -y install i2c-tools python3-smbus
をインストールしてから、smbusをimportして使う
"""

import smbus                #I2C通信するためのモジュールsmbusをインポートする
import time                 #sleepするためにtimeモジュールをインポートする

class I2C:
    def __init__(self):
        self.bus = smbus.SMBus(1)   # I2C通信するためのモジュールsmbusのインスタンスを作成
        self.adress = 0x04               # arduinoのサンプルプログラムで設定したI2Cアドレス
        
    def i2c_write(self, val, vals):
        # 1byte(1文字)送信コマンド
        self.bus.write_byte(self.adress, val)   # 1文字はアスキーコードで送るので、val = ord('字')で送る

        # 1byte(1文字)送信コマンド(cmdコマンド付き)
        self.bus.write_byte_data(self.adress, 0x80, val) # cmd = 0x00で,制御コマンド。cmd = 0x80で、データコマンド
        self.bus.write_word_data(self.adress, 0x80, val)

        # リストを使って、連続でbyteデータを送信する
        self.bus.write_block_data(self.adress, 0x80, [vals])     # [vals] = ['a', 'b', 'c']とリストにする
        self.bus.write_i2c_block_data(self.adress, 0x80, [vals])

        # I2C機器に送信開始を知らせるために使う
        self.bus.write_quick(self.adress)   # time.sleep(0.1)と一緒に使う
        # time.sleep(0.1)
        

    def i2c_read(self, lists_no):
        moji = ""
        lists = []

        # 1byteだけ受信
        moji = chr(self.bus.read_byte(self.adress))  

        # 1byteだけ受信（cmdコマンド付き)
        moji = chr(self.bus.read_byte_data(self.adress, 0x00))     # cmd = 0x00で,制御コマンド。cmd = 0x80で、データコマンド
        moji = chr(self.bus.read_word_data(self.adress, 0x00))
        
        # 連続データをリストで受け取る
        lists = self.bus.read_i2c_block_data(self.adress, 0x00, lists_no)  # lists_noには送られてくるデータを受け取る数を指定（最高32byte）
        # lists = self.bus.read_block_data(self.adress, 0x00)    # 使うとフリーズする

if __name__ == '__main__':
    bus = smbus.SMBus(1)    ##I2C通信するためのモジュールsmbusのインスタンスを作成
    adress = 0x04           #arduinoのサンプルプログラムで設定したI2Cチャンネル
    retu = [ord('A'), ord('B'), ord('C'), ord('D'), ord('E')]
    lists = []
    lists2 = []

    # 5文字のリストを送信
    bus.write_i2c_block_data(adress, 0x80, retu) 

    # 5文字のリストを受信
    lists = bus.read_i2c_block_data(adress, 0x00, 5)
    for i in lists:
        lists2.append(chr(i))
    print(lists2)