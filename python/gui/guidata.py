# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from ttkthemes import *


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        frame1 = ttk.Frame(master, padding=16)
        label1 = ttk.Label(frame1, text='Your name')
        t = tk.StringVar()
        entry1 = ttk.Entry(frame1, textvariable=t)
        button1 = ttk.Button(
            frame1,
            text='OK',
            command=lambda: print('Hello, %s.' % t.get())
        )

        frame2 = ttk.Frame(master, padding=16)
        label2 = ttk.Label(frame2, text='aaa')
        t2 = tk.StringVar()
        entry2 = ttk.Entry(frame2, textvariable=t2)

        # レイアウト
        frame1.pack()
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        button1.grid(row=1, column=1)
        frame2.pack()
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)


if __name__ == '__main__':
    # ルートウィンドウ要素の作成
    root = tk.Tk()

    # ウィンドウタイトルの設定
    root.title('ウィンドウタイトル')

    # クラス呼び出し
    Application(master=root)

    root.mainloop()
