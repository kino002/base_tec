import smbus

class HIH6130:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.adress = 0x27

        self.data = []

    def ondo_shitudo_get(self):
        self.data = self.bus.read_i2c_block_data(self.adress, 0x80, 4)

        # 受信したデータを変換
        h = ((self.data[0] & 0x3f) << 8) | self.data[1]
        humi = float(h) / 16383 * 100
        t = (self.data[2] << 6) | (self.data[3] >> 2)
        temp = float(t) / 16383 * 165 - 40

        # 桁数を小数点以下第一位に揃える
        humi = str(humi)
        temp = str(temp)
        humi2 = ""
        temp2 = ""
        for i in range(4):
            humi2 = humi2 + humi[i]
            temp2 = temp2 + temp[i]
        humi2 = float(humi2)
        temp2 = float(temp2)
        
        return humi2, temp2
        # 温度、湿度の表示
        # print("温度: {}度, 湿度: {}%".format(temp2, humi2))

if __name__ == "__main__":
    humi, temp = HIH6130().ondo_shitudo_get()
    print("温度: {}度, 湿度: {}%".format(temp, humi))
