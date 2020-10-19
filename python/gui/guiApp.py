# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog as fd
import os
import sqlite3
import pandas as pd


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.root = master

        # ウィンドウタイトルの設定
        master.title(u'物品検索')

        # ウィンドウの大きさの変更を規定
        master.resizable(width=False, height=False)

        # ウィンドウのグリッドを 1x1 にする
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 下部バーのスタイル作成
        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure(
            'MyWidget.TButton',
            background='DarkGoldenrod3',
            borderwidth=0,
            shiftrelief=0,
            relief='flat',
            font=('游明朝', '12')
        )

        # ページのスタイル作成
        self.ss = ttk.Style()
        self.ss.configure(
            'Page.TButton',
            background='SlateGray4',
            borderwidth=0,
            shiftrelief=0,
            relief='flat'
        )

        # ボタンのスタイル作成
        self.sss = ttk.Style()
        self.sss.configure(
            'Button.TButton',
            width=8,
            height=3,
            background='DarkGoldenrod3',
            relief='groove'
        )

        # コンボボックスのスタイル作成
        self.s4 = ttk.Style()
        self.s4.configure(
            'MyWidget.TCombobox',
            width=8,
            height=3,
            background='DarkGoldenrod3',
            relief='groove'
        )

        # -----物品検索フレーム-----------------------------
        # 物品検索ページフレーム作成
        self.frame_material = ttk.Frame(
            master,
            padding=18,
            style='Page.TButton'
        )
        self.frame_material.grid(row=0, column=0, sticky=tk.N+tk.W+tk.S+tk.E)

        # ページタイトル作成
        self.title_material = makeTitle(
            parent=self.frame_material,
            file_path='./image/server.png',
            title='物品検索'
        )

        # 物品検索ページのウィジェット作成
        self.makePageMaterial(self.frame_material)
        # --------------------------------------------------

        # -----組織検索フレーム------------------------------
        # 組織検索ページフレーム作成
        self.frame_organization = ttk.Frame(
            master,
            padding=18,
            style='Page.TButton'
        )
        self.frame_organization.grid(
            row=0, column=0, sticky=tk.N+tk.W+tk.S+tk.E)

        # ページタイトル作成
        self.title_organization = makeTitle(
            parent=self.frame_organization,
            file_path='./image/shakehand.png',
            title='組織検索'
        )

        # --------------------------------------------------
        # -----連絡先検索フレーム----------------------------
        # 連絡先検索ページフレーム作成
        self.frame_contact = ttk.Frame(
            master,
            padding=18,
            style='Page.TButton'
        )
        self.frame_contact.grid(row=0, column=0, sticky=tk.N+tk.W+tk.S+tk.E)

        # ページタイトル作成
        self.title_contact = makeTitle(
            parent=self.frame_contact,
            file_path='./image/phone.png',
            title='連絡先検索'
        )
        # --------------------------------------------------

        # -----csvインポート検索フレーム---------------------
        # csvインポートページフレーム作成
        self.frame_import = ttk.Frame(
            master,
            padding=16,
            style='Page.TButton'
        )
        self.frame_import.grid(row=0, column=0, sticky=tk.N+tk.W+tk.S+tk.E)

        # ページタイトル作成
        self.title_import = makeTitle(
            parent=self.frame_import,
            file_path='./image/file.png',
            title='csvインポート'
        )

        # csvインポートページのウィジェット作成
        self.makePageImport(self.frame_import)
        # --------------------------------------------------

        # -----設定フレーム----------------------------------
        # 設定ページフレーム作成
        self.frame_setting = ttk.Frame(
            master,
            padding=18,
            style='Page.TButton'
        )
        self.frame_setting.grid(row=0, column=0, sticky=tk.N+tk.W+tk.S+tk.E)

        # ページタイトル作成
        self.title_setting = makeTitle(
            parent=self.frame_setting,
            file_path='./image/setting.png',
            title='アプリ設定'
        )

        # ウィジェット作成
        self.makePageSetting(self.frame_setting)
        # --------------------------------------------------

        # -----画面遷移ボタンの作成-------------------------
        # 画面下部バーの設定
        self.makeFrameUnder(master)
        # -------------------------------------------------

        # -----フッターの作成-------------------------------
        self.makeFooter(master)
        # -------------------------------------------------

        # frame_materialを一番上に表示
        self.frame_material.tkraise()

    def changePage(self, page):
        page.tkraise()

    def makePageMaterial(self, parent):
        # 検索フレーム
        self.frame_search = ttk.Frame(
            parent,
            style='Page.TButton')
        self.frame_search.pack(expand=False, fill=tk.X)

        # 検索対象ラベル作成
        self.label1 = ttk.Label(
            self.frame_search,
            text='検索対象',
            style='Page.TButton',
            font=('游明朝', '12')
        )
        self.label1.grid(row=0, column=0, sticky=tk.W, pady=5)

        # 検索列設定コンボボックス作成
        # 項目作成
        self.types = (u'物品コード', u'カナ品名')

        # コンボボックスの変数作成
        self.combovalue = tk.StringVar()

        # コンボボックス作成
        self.combo1 = ttk.Combobox(
            self.frame_search,
            state='readonly',
            value=self.types,
            font=('游明朝', '12'),
            textvariable=self.combovalue,
            style='MyWidget.TCombobox'
        )
        # 初期選択値設定
        self.combo1.current(0)
        self.combo1.grid(row=0, column=1, pady=5, sticky=tk.W)

        # 検索ワードラベル作成
        self.label5 = ttk.Label(
            self.frame_search,
            text='検索ワード',
            style='Page.TButton',
            font=('游明朝', '12')
        )
        self.label5.grid(row=1, column=0, pady=5, sticky=tk.W)

        # 検索ワードエントリーの作成
        self.t = tk.StringVar()
        self.entry_search = ttk.Entry(
            self.frame_search,
            textvariable=self.t,
            width=40,
            font=('游明朝', '12')
        )
        self.entry_search.grid(row=1, column=1, pady=5, sticky=tk.W)

        # 検索ボタン
        self.button1 = ttk.Button(
            self.frame_search,
            text=u'検 索',
            command=lambda: self.makePageTable(),
            style='Button.TButton'
        )
        self.button1.grid(row=1, column=2, pady=5, padx=2)

    def makePageSetting(self, parent):
        # テーマ1ウィジェット群作成
        self.widgets_setting1 = makeSettingWidget(
            parent=parent,
            text='テーマ1'
        )

        # テーマ2ウィジェット群作成
        self.widgets_setting2 = makeSettingWidget(
            parent=parent,
            text='テーマ2'
        )

    def makeFooter(self, master):
        # ページフレーム作成
        self.frame_status = ttk.Frame(
            master
        )
        self.frame_status.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.label_status = ttk.Label(
            self.frame_status,
            text='guiApp(ver.1.0) <latest update @2020.10>',
            font=('游明朝', '8')
        )
        self.label_status.pack(side=tk.RIGHT, fill=tk.X)

    def makePageTable(self):
        # ルートウィンドウ要素の作成
        root = tk.Toplevel(self.root)

        root.geometry('600x400')

        # クラス呼び出し
        Table(
            master=root,
            keyword=self.t.get(),
            column=self.combovalue.get()
        )

        root.mainloop()

    def makePageImport(self, frame_parent):
        # csvファイル1ウィジェット群作成
        self.widgets_csv = makeCSVWidget(
            parent=frame_parent, dbname='./materialDB.db')

        # csvファイル2ウィジェット群作成
        self.widgets_csv2 = makeCSVWidget(
            parent=frame_parent, dbname='./material2DB.db')

    def makeFrameUnder(self, frame_parent):
        # ウィンドウ下部バーフレームの作成
        self.frame_bar = ttk.Frame(
            frame_parent,
            style='MyWidget.TButton',
            padding=5,
        )
        self.frame_bar.grid(row=1, column=0, sticky=tk.W+tk.E)

        # 物品検索ボタンフレーム
        self.button_material = makeButton(
            move_page=self.frame_material,
            parent=self.frame_bar,
            image_path='./image/server.png',
            label_name='物品検索',
            order=0
        )

        # 組織検索ボタンフレーム
        self.button_organization = makeButton(
            move_page=self.frame_organization,
            parent=self.frame_bar,
            image_path='./image/shakehand.png',
            label_name='組織検索',
            order=1
        )

        # 連絡先検索ボタンフレーム
        self.button_contact = makeButton(
            move_page=self.frame_contact,
            parent=self.frame_bar,
            image_path='./image/phone.png',
            label_name='連絡先検索',
            order=2
        )

        # csvインポートフレーム
        self.button_import = makeButton(
            move_page=self.frame_import,
            parent=self.frame_bar,
            image_path='./image/file.png',
            label_name='csvインポート',
            order=3
        )

        # 設定フレーム
        self.button_setting = makeButton(
            move_page=self.frame_setting,
            parent=self.frame_bar,
            image_path='./image/setting.png',
            label_name='アプリ設定',
            order=3
        )


class Table(ttk.Frame):
    def __init__(self, master, keyword, column, frmprev=None, lastid=0):
        ttk.Frame.__init__(self, master)

        self.master = master

        # Treeウィジェットのスタイル作成
        self.s1 = ttk.Style()
        self.s1.configure(
            'MyWidget.Treeview',
            background='SlateGray4',
            borderwidth=0,
            shiftrelief=0,
            relief='White',
            font=('游明朝', '12')
        )

        # Treeウィジェットのスタイル作成
        self.s2 = ttk.Style()
        self.s2.configure(
            'MyWidget.Horizontal.TScrollbar',
            background='White',
            borderwidth=0,
            shiftrelief=0,
            relief='flat',
            font=('游明朝', '10')
        )

        self.s3 = ttk.Style()
        self.s3.configure(
            'MyWidget.Vertical.TScrollbar',
            background='White',
            borderwidth=0,
            shiftrelief=0,
            relief='flat',
            font=('游明朝', '10')
        )

        self.s4 = ttk.Style()
        self.s4.configure(
            'MyWidget.TFrame',
            background='White'
        )

        self.s5 = ttk.Style()
        self.s5.configure(
            'Move.TButton',
            background='White',
            relief='flat'
        )

        # ウィンドウタイトルの設定
        master.title(u'検索結果')

        # 表フレーム作成
        self.frame_table = ttk.Frame(
            master,
            style='MyWidget.TFrame'
        )
        self.frame_table.place(
            relheight=1.0,
            relwidth=1.0,
            relx=0.0,
            rely=0.0
        )

        # 表の作成
        self.tree = ttk.Treeview(
            self.frame_table,
            style='Mywidget.Treeview'
        )

        # 列名IDの設定
        lst_id = list(range(0, 17))
        tpl_id = tuple(lst_id)
        self.tree['columns'] = tpl_id

        # アイコン列を表示しない
        self.tree['show'] = 'headings'

        # 列のプロパティを設定
        for id in tpl_id:
            self.tree.column(id, width=150, minwidth=50, stretch=tk.YES)

        # 列名の定義
        lst_column_name = [
            'id',
            '物品コード',
            '購入識別',
            'カナ品名',
            '単位',
            '要求区分',
            'ストック区分',
            '仕様書番号',
            '在庫品単価',
            '再用品単価',
            '在庫品ダム付単価',
            '再用品ダム付単価',
            '主指定表示',
            'ガードタイム',
            '直送数量倉庫',
            '直送数量支店等',
            '備考',
        ]

        # 列名の設定
        for id in tpl_id:
            self.tree.heading(id, text=lst_column_name[id], anchor=tk.W)

        self.tree.configure(displaycolumns=list(range(1, 17)))

        # insert
        rst = self.insertToTree(
            tree=self.tree,
            dbname='./materialDB.db',
            keyword=keyword,
            column=column,
            lastid=lastid
        )

        self.tree.place(
            relheight=0.9,
            relwidth=0.95,
            relx=0.0,
            rely=0.0
        )

        # スクロールバーの作成
        # 横方向
        self.bar_x = ttk.Scrollbar(
            self.frame_table,
            orient=tk.HORIZONTAL,
            style='MyWidget.Horizontal.TScrollbar'
        )
        self.bar_x.place(
            relheight=0.05,
            relwidth=0.95,
            relx=0.0,
            rely=0.85
        )
        self.bar_x.config(command=self.tree.xview)

        # 縦方向
        self.bar_y = ttk.Scrollbar(
            self.frame_table,
            orient=tk.VERTICAL,
            style='MyWidget.Vertical.TScrollbar'
        )
        self.bar_y.place(
            relheight=0.85,
            relwidth=0.05,
            relx=0.95,
            rely=0.0
        )
        self.bar_y.config(command=self.tree.yview)

        # ウィジェットとスクロールバーの紐づけ
        self.tree.config(
            yscrollcommand=lambda f, l: self.bar_y.set(f, l),
            xscrollcommand=lambda f, l: self.bar_x.set(f, l)
        )

        # 遷移ボタンフレームの作成
        self.frame_mv = ttk.Frame(
            self.frame_table,
            style='MyWidget.TFrame'
        )
        self.frame_mv.place(
            relheight=0.1,
            relwidth=1.0,
            relx=0.0,
            rely=0.9
        )

        if lastid != 0:
            # 前へボタンフレーム作成
            self.frame_prev = ttk.Frame(
                self.frame_mv
            )
            self.frame_prev.pack(side=tk.LEFT, anchor=tk.W)

            # イメージの作成
            self.imageprev = Image.open('./image/arrow_prev.png')
            self.imageprev = self.imageprev.resize((30, 30))
            self.imgprev = ImageTk.PhotoImage(self.imageprev)

            # 前へボタン作成
            self.button_prev = ttk.Button(
                self.frame_prev,
                style='Move.TButton',
                image=self.imgprev,
                command=lambda: frmprev.tkraise()
            )
            self.button_prev.pack()

        if rst[0] is False:
            # 次へボタンフレーム作成
            self.frame_next = ttk.Frame(
                self.frame_mv
            )
            self.frame_next.pack(side=tk.RIGHT, anchor=tk.E)

            # イメージの作成
            self.imagenext = Image.open('./image/arrow_next.png')
            self.imagenext = self.imagenext.resize((30, 30))
            self.imgnext = ImageTk.PhotoImage(self.imagenext)

            # 次へボタン作成
            self.button_next = ttk.Button(
                self.frame_next,
                style='Move.TButton',
                image=self.imgnext,
                command=lambda: Table(master=master,
                                      keyword=keyword,
                                      column=column,
                                      frmprev=self.frame_table,
                                      lastid=rst[1])
            )
            self.button_next.pack()

        self.frame_table.tkraise()

    def insertToTree(self, tree, dbname, keyword, column, lastid):
        try:
            # DBへ接続
            conn = sqlite3.connect(dbname, isolation_level='EXCLUSIVE')

            # DB上の処理対象の行を指し示すためのcursorオブジェクト作成
            cur = conn.cursor()

            # query文の作成
            # collate_nocase
            collate_nocase = 'COLLATE NOCASE'

            # 並び順
            order = 'ORDER BY id'

            # 制限
            lim_n = 30
            lim = 'LIMIT ' + str(lim_n)
            # ページネーション適用時コメントアウトすること
            lim = ''

            # ワイルドカードが入っている場合,LIKE句を使う
            if '*' in keyword:
                op = 'LIKE ? '
            else:
                op = '= ? '

            # ワイルドカードをLike句に置換
            keyword = keyword.replace('*', '%')

            # 検索文字列に'をつけてタプル化
            tpl_keyword = (lastid, "'" + str(keyword) + "'")

            query = 'SELECT * FROM DBM WHERE ' + 'id >= ? AND ' + column + ' ' + \
                collate_nocase + ' ' + op + order + ' ' + lim + ';'
            
            # レコードを表へ挿入
            lst = [[s.replace("'", "") if type(
                    s) == str else s for s in row] for row in cur.execute(query, tpl_keyword)]
    
            # 終了判定
            if len(lst) < lim_n or lim == '':
                flgEnd = True
            else:
                flgEnd = False

            # 取得した最後のレコードのidを取得
            if len(lst) != 0:
                next_id = lst[-1][0] + 1
            else:
                next_id = None

            # 表へ挿入
            for r in lst:
                tree.insert('', "end", values=r)
            # commit
            conn.commit()

        except Exception:
            # エラーメッセージ
            messagebox.showerror(
                title='Error',
                message='データベース検索中にエラーが発生しました．'
            )

            conn.rollback()

        finally:
            # 閉じる
            conn.close()

            return flgEnd, next_id


class makeTitle(Application):
    def __init__(self, parent, file_path, title):
        # ページタイトルフレーム作成
        self.frame_title = ttk.Frame(
            parent,
            style='Page.TButton'
        )
        self.frame_title.pack(anchor=tk.NW)

        # イメージの作成
        self.image = Image.open(file_path)
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)

        # イメージラベル作成
        self.label_icon = ttk.Label(
            self.frame_title,
            image=self.img,
            style='Page.TButton'
        )
        self.label_icon.pack(side=tk.LEFT, anchor=tk.W)

        # タイトルラベル作成
        self.label_title = ttk.Label(
            self.frame_title,
            text=title,
            style='Page.TButton',
            font=('游明朝', '18')
        )
        self.label_title.pack(anchor=tk.W, side=tk.LEFT)


class makeCSVWidget(Application):
    def __init__(self, parent, dbname):
        # csvファイル1 フレーム作成
        self.frame = ttk.Frame(
            parent,
            style='Page.TButton'
        )
        self.frame.pack(anchor=tk.CENTER, pady=10)

        # csvファイル1 ラベル作成
        self.label = ttk.Label(
            self.frame,
            text='csvファイル1',
            style='Page.TButton',
            font=('游明朝', '12')
        )
        self.label.grid(row=0, column=0, sticky=tk.W)

        # csvファイル1 エントリー作成
        t = tk.StringVar()
        self.entry = ttk.Entry(
            self.frame,
            textvariable=t,
            width=40,
            font=('游明朝', '12')
        )
        self.entry.grid(row=1, column=0, sticky=tk.W)

        # csvファイル1 参照ボタン作成
        self.button_reference = ttk.Button(
            self.frame,
            text=u'参 照',
            command=lambda: self.showDialog(),
            style='Button.TButton',
        )
        self.button_reference.grid(
            row=1,
            column=1,
            sticky=tk.W,
            padx=5
        )

        # csvファイル1 importボタン作成
        self.button_import = ttk.Button(
            self.frame,
            text='Import',
            style='Button.TButton',
            command=lambda: self.importCSV(dbname)
        )
        self.button_import.grid(row=2, column=0, sticky=tk.W)

    def showDialog(self):
        fTyp = [("csvファイル", "csv")]
        Dir = os.path.abspath(os.path.dirname(__file__))
        file_name = fd.askopenfilename(filetypes=fTyp, initialdir=Dir)

        if file_name == "":
            return
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, file_name)

    def create_table(self, conn, cur):
        # テーブルの削除
        cur.execute('DROP TABLE IF EXISTS DBM;')

        # 削除した領域の解放
        cur.execute('VACUUM;')

        # テーブルの作成
        cur.execute("""
        CREATE TABLE IF NOT EXISTS DBM(
            id INTEGER,
            物品コード TEXT,
            購入識別 TEXT,
            カナ品名 TEXT,
            単位 TEXT,
            要求区分 TEXT,
            ストック区分 TEXT,
            仕様書番号 TEXT,
            在庫品単価 TEXT,
            再用品単価 TEXT,
            在庫品ダム付単価 TEXT,
            再用品ダム付単価 TEXT,
            主指定表示 TEXT,
            ガードタイム TEXT,
            直送数量倉庫 TEXT,
            直送数量支店等 TEXT,
            備考 TEXT,
            PRIMARY KEY(id, 物品コード, カナ品名)
            );""")

    def importCSV(self, dbname):
        try:
            # DBを作成して，DBに接続する
            conn = sqlite3.connect(dbname, isolation_level='EXCLUSIVE')

            # DB上の処理対象の行を指し示すためのcursorオブジェクト作成
            cur = conn.cursor()

            # テーブル作成
            self.create_table(conn, cur)

            path = str(self.entry.get())

            if path == "":
                return

            # csvを開く
            df = pd.read_csv(path, encoding='cp932', index_col=None)

            # データ整形
            df = self.arrangeDB(df)

            # tableに各行のデータを挿入する
            df.to_sql('DBM', conn, if_exists='replace', index=False)

            # コミット
            conn.commit()

            # 終了メッセージ
            messagebox.showinfo(
                title='Information',
                message='データベースへのインポートが完了しました．'
            )

        except Exception:
            # エラーメッセージ
            messagebox.showerror(
                title='Error',
                message='インポート中にエラーが発生しました．'
            )

            conn.rollback()

        finally:
            # 閉じる
            conn.close()

    def arrangeDB(self, df):
        # 使わないカラムを削除(INSERT文が遅いので)
        df = df.drop('機械処理年月日', axis=1)
        df = df.drop('西暦年度', axis=1)
        df = df.drop('ダミー1', axis=1)
        df = df.drop('ダミー2', axis=1)
        df = df.drop('Unnamed: 20', axis=1)
        df = df.drop('Unnamed: 21', axis=1)
        df = df.drop('Unnamed: 22', axis=1)

        # id行の挿入
        df.insert(0, 'id', list(range(0, len(df))))

        return df


class makeSettingWidget():
    def __init__(self, parent, text):
        s = ttk.Style()
        s.configure(
            'Setting.TButton',
            background='SlateGray4',
            borderwidth=1,
            font=('游明朝', '12')
        )

        # フレーム作成
        self.frame = ttk.Frame(
            parent,
            style='Setting.TButton',
            padding=5
        )
        self.frame.pack(side=tk.TOP, anchor=tk.CENTER)

        # フレームキャンバス
        self.frame_canvas = ttk.Frame(
            self.frame,
            style='Page.TButton',
            padding=5
        )
        self.frame_canvas.pack(side=tk.LEFT)

        # キャンバス作成
        self.canvas = tk.Canvas(
            self.frame_canvas,
            width=20,
            height=20,
            bg='SlateGray4'
        )
        self.canvas.pack(side=tk.LEFT)

        # フレームラベル&パレット
        self.frame_palette = ttk.Frame(
            self.frame,
            style='Page.TButton',
            padding=5
        )
        self.frame_palette.pack(side=tk.LEFT)

        # ラベル作成
        self.label = ttk.Label(
            self.frame_palette,
            text=text,
            style='Page.TButton',
            font=('游明朝', '12')
        )
        self.label.grid(row=0, column=0)

        # カラーパレットボタン作成
        self.button_palette = ttk.Button(
            self.frame_palette,
            text=u'パレット',
            command=lambda: self.showColorPalette,
            style='Button.TButton',
        )
        self.button_palette.grid(
            row=1,
            column=0
        )

    def showColorPalette(self):
        pass


class makeButton(Application):
    def __init__(self, move_page, parent, image_path, label_name, order):
        # イメージの作成
        image = Image.open(image_path)
        image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(image)

        self.frame_button = ttk.Frame(
            parent,
            style='MyWidget.TButton'
        )
        self.frame_button.pack(side=tk.LEFT, padx=20)

        # 遷移ボタン作成
        self.button_change = ttk.Button(
            self.frame_button,
            command=lambda: self.changePage(move_page),
            image=self.img,
            style='MyWidget.TButton'
        )
        self.button_change.grid(row=0, column=order)

        # ラベル作成
        self.label_change = ttk.Label(
            self.frame_button,
            text=label_name,
            style='MyWidget.TButton'
        )
        self.label_change.grid(row=1, column=order)


if __name__ == '__main__':
    # ルートウィンドウ要素の作成
    root = tk.Tk()

    # クラス呼び出し
    Application(master=root)

    root.mainloop()
