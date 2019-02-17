import tkinter

root = tkinter.Tk()
root.title("ロボットコントロール")
root.minsize(300, 300)

# ボタン作成
mae_button = tkinter.Button(text="前進(W)")
mae_button.place(x=100, y=50)
ushiro_button = tkinter.Button(text="後退(S)")
ushiro_button.place(x=100, y=150)
teishi_button = tkinter.Button(text="停止(Space)")
teishi_button.place(x=100, y=100)
migi_button = tkinter.Button(text="右旋回(D)")
migi_button.place(x=210, y=100)
hidari_button = tkinter.Button(text="左旋回(A)")
hidari_button.place(x=10, y=100)

# イベント作成
def mae_button_click():
    print("{}が押されました。".format("前進(W)")) 
def ushiro_button_click():
    print("{}が押されました。".format("後退(S)"))
def teishi_button_click():
    print("{}が押されました。".format("停止(space)"))
def migi_button_click():
    print("{}が押されました。".format("右旋回(D)"))
def hidari_button_click():
    print("{}が押されました。".format("左旋回(A)"))

def mae_click(event):                           # ()内に引数を上取れるようにeventを設定。（引数を受け取るようにしないと、エラーがでる。)
    print("{}が押されました。".format("w"))
def ushiro_click(event):
    print("{}が押されました。".format("s"))
def teishi_click(event):
    print("{}が押されました。".format("space"))
def migi_click(event):
    print("{}が押されました。".format("d"))
def hidari_click(event):
    print("{}が押されました。".format("a"))

# ボタンが押されたら
mae_button["command"] = mae_button_click
ushiro_button["command"] = ushiro_button_click
teishi_button["command"] = teishi_button_click
migi_button["command"] = migi_button_click
hidari_button["command"] = hidari_button_click

# キーボード操作

root.bind('<Key-w>', mae_click)         # キーは<Key-*>で設定する。
root.bind('<Key-s>', ushiro_click)
root.bind('<Key-space>', teishi_click)
root.bind('<Key-d>', migi_click)
root.bind('<Key-a>', hidari_click)

root.mainloop()