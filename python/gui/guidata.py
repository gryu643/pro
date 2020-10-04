# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # ウィンドウタイトルの設定
        master.title(u'物品検索')

        # ウィンドウの大きさを指定
        master.geometry('800x600')

        # ウィンドウのグリッドを 1x1 にする
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # -----物品検索フレーム-----------------------------
        # 物品検索ページフレーム作成
        self.frame_material = ttk.Frame(master, padding=16)

        self.frame_material.grid(row=0, column=0, sticky='NSEW')

        # 検索フレーム
        self.frame_search = ttk.Frame(self.frame_material)
        self.frame_search.pack(expand=False, fill=tk.X)

        # 検索対象ラベル作成
        self.label1 = ttk.Label(self.frame_search, text='検索対象：')
        self.label1.grid(row=0, column=0)

        # 検索列設定コンボボックス作成
        # 項目作成
        self.types = (u'物品コード', u'カナ品名')

        # コンボボックスの変数作成
        self.combovalue = tk.StringVar()

        # コンボボックス作成
        self.combo1 = ttk.Combobox(
            self.frame_search, state='readonly', value=self.types,
            textvariable=self.combovalue
        )

        # 初期選択値設定
        self.combo1.current(0)

        self.combo1.grid(row=0, column=1)

        #
        self.label5 = ttk.Label(self.frame_search, text='検索ワード')
        self.label5.grid(row=1, column=0, pady=5)

        # 検索ワードエントリーの作成
        self.t = tk.StringVar
        self.entry1 = ttk.Entry(self.frame_search, textvariable=self.t)
        self.entry1.grid(row=1, column=1, pady=5)

        # 検索ボタン
        self.button1 = ttk.Button(
            self.frame_search,
            text=u'検索',
            command=lambda: self.get_keyword()
        )
        self.button1.grid(row=1, column=2, pady=5)

        # 表フレーム作成
        self.frame_table = ttk.Frame(self.frame_material)
        self.frame_table.pack(expand=False, fill=tk.X)

        # 表の作成
        self.tree = ttk.Treeview(self.frame_table)

        # 列の定義
        self.tree['columns'] = (1, 2, 3, 4)
        self.tree['show'] = 'headings'
        self.tree.column(1, width=190, minwidth=190, stretch=tk.NO)
        self.tree.column(2, width=190, minwidth=190, stretch=tk.NO)
        self.tree.column(3, width=190, minwidth=190, stretch=tk.NO)
        self.tree.column(4, width=190, minwidth=190, stretch=tk.NO)

        # 見出しの定義
        self.tree.heading(1, text='index', anchor=tk.W)
        self.tree.heading(2, text='name', anchor=tk.W)
        self.tree.heading(3, text='num', anchor=tk.W)
        self.tree.heading(4, text='value', anchor=tk.W)

        # insert
        self.tree.insert('', "end", values=('1', 'apple', '2', '100'))
        self.tree.insert('', "end", values=('2', 'orange', '5', '120'))
        self.tree.insert('', "end", values=('3', 'grape', '1', '300'))
        self.tree.insert('', "end", values=('4', 'pineapple', '0', '200'))

        self.frame_table.grid_propagate(False)

        self.tree.pack(pady=10, side=tk.TOP, fill=tk.X)

        # 下バー
        self.canvas1 = tk.Canvas(
            self.frame_material, width=100, height=50, bg='blue')

        # --------------------------------------------------
        # -----組織検索フレーム------------------------------
        # 組織検索ページフレーム作成
        self.frame_organization = ttk.Frame(master, padding=16)

        self.frame_organization.grid(row=0, column=0, sticky='nsew')

        self.label2 = ttk.Label(self.frame_organization, text='組織検索画面',
                                anchor='center', font=('Helvetica', '35'))

        self.label2.pack()

        # --------------------------------------------------
        # -----連絡先検索フレーム----------------------------
        # 連絡先検索ページフレーム作成
        self.frame_contact = ttk.Frame(master, padding=16)

        self.frame_contact.grid(row=0, column=0, sticky='nsew')

        self.label3 = ttk.Label(self.frame_contact, text='連絡先検索画面',
                                anchor='center', font=('Helvetica', '35'))

        self.label3.pack()
        # --------------------------------------------------
        # -----csvインポート検索フレーム---------------------
        # csvインポートページフレーム作成
        self.frame_import = ttk.Frame(master, padding=16)

        self.frame_import.grid(row=0, column=0, sticky='nsew')

        self.label4 = ttk.Label(self.frame_import, text='csvインポート画面',
                                anchor='center', font=('Helvetica', '35'))

        self.label4.pack()
        # --------------------------------------------------

        # frame_materialを一番上に表示
        self.frame_material.tkraise()

    def change_page(self, page):
        page.tkraise()

    def get_keyword(self):
        # キーワードを取得する
        print(self.combovalue.get())


if __name__ == '__main__':
    # ルートウィンドウ要素の作成
    root = tk.Tk()

    # クラス呼び出し
    Application(master=root)

    root.mainloop()
