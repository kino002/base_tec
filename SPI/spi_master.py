import time
import spidev
 
CE = 0                   # 接続するCE0/CE1ポートを設定

spi = spidev.SpiDev()    # spi通信するためのインスタンスを作成
spi.open(0, CE)          # open(bus, CE)で、busには0を指定
spi.mode = 0b01          # モード1で通信する(モードは４つある)
spi.max_speed_hz = 9600  # 通信速度設定
 


def getdata(data):
    result = spi.xfer2([data])  # リストを送ると戻ってくるリストを受け取る
                                # [data, data2, data3]と数を増やして送ることもできる。
    if result ==  [55]:         # 戻ってきたデータに対して処理をする
        print("Hello World!")
    
if __name__ == '__main__':
  try:
    while True:
      getdata(78)
      time.sleep(1)
  except KeyboardInterrupt:
    spi.close()                 # spi通信を終了する
