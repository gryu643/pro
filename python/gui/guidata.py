from tkinter import *
from tkinter import ttk

# ルートウィンドウ要素の作成
root = Tk()

# ウィンドウタイトルの設定
root.title('ウィンドウタイトル')

frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='Your name')
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print('Hello, %s.' % t.get())
)

frame2 = ttk.Frame(root, padding=16)
label2 = ttk.Label(frame1, text='aaa')

# レイアウト
frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)
frame2.pack()
label2.pack(side=LEFT)


root.mainloop()
