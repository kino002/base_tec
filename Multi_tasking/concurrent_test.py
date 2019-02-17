# スレッドプール(concurrent.futures)でマルチタスクプログラムを動かす

import concurrent.futures
from time import sleep

def test1():
    while True:
        print("test1")
        sleep(1)

def test2(data):
    while True:
        print(data)
        sleep(1)

if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2) # 同時に動かす最大数(max_workers)を決めるとスレッドを使いまわしてくれる
    executor.submit(test1)  # ()内に関数を()無しで指定。関数()無しは、待機状態のこと。
    executor.submit(test2("test222")) # 関数に引数を渡す場合は、関数()も使える。