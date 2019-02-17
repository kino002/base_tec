# スレッド(threading)でマルチタスクプログラムを動かす

import threading
from time import sleep

def test1():
    while True:
        print("test1")
        sleep(1)

def test2():
    while True:
        print("test2")
        sleep(1)

if __name__ == "__main__":
    thread_1 = threading.Thread(target=test1)   # targetに関数を()無しで渡す
    thread_2 = threading.Thread(target=test2)

    thread_1.start()    # .start()でプログラムスタート
    thread_2.start()