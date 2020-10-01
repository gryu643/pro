
import tkinter
from tkinter import ttk, scrolledtext

# メインウィンドウ
main_window = tkinter.Tk()
main_window.title('mo22comi')
main_window.geometry('600x830')

# メインフレーム
main_frame = ttk.Frame(main_window)
main_frame.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

text_frame = ttk.Frame(main_window)
text_frame.grid(column=0, row=1, sticky=tkinter.NSEW, padx=5, pady=10)

# ログフレーム
log_frame = ttk.Frame(main_window)
log_frame.grid(column=0, row=2, sticky=tkinter.NSEW, padx=5, pady=10)

# ウィジェット作成
file_label = ttk.Label(main_frame, text='データ')
file_box = ttk.Entry(main_frame)
file_btn = ttk.Button(main_frame, text='参照')
entry_label = ttk.Label(main_frame, text='エントリー')
entry_box = ttk.Entry(main_frame)

text_label = ttk.Label(text_frame, text='テキスト', font='游明朝')
text_box = scrolledtext.ScrolledText(text_frame)

log_label = ttk.Label(log_frame, text='ログ')
log_box = scrolledtext.ScrolledText(log_frame)

# ウィジェットの配置
file_label.grid(column=0, row=0, pady=10, padx=5)
file_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
file_btn.grid(column=2, row=0, padx=5)

entry_label.grid(column=0, row=1)
entry_box.grid(column=1, row=1, sticky=tkinter.EW, pady=10, padx=5)

text_label.grid(column=0, row=0, sticky=tkinter.NW, padx=5)
text_box.grid(column=0, row=1, pady=5, padx=5)

log_label.grid(column=0, row=0, sticky=tkinter.NW, padx=5)
log_box.grid(column=0, row=1, pady=10, padx=5)

# 配置設定
main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

main_window.mainloop()
