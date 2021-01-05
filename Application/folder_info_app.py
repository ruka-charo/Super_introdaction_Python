import datetime
import os
import os.path
import tkinter as tk


#ウインドウの作成
base = tk.Tk()
base_2 = tk.Tk()
base.geometry('550x100')
base_2.geometry()

#ラベルの作成
string = tk.StringVar()

label = tk.Label(base, text='フォルダ内ファイルについて\
「サイズ」、「作成時刻」、「最終アクセス時刻」を表示します。\
\n情報を引き出すフォルダのパスを入力してください。').pack()
entry = tk.Entry(base, width=55)
entry.insert(tk.END, '')
entry.pack()


#情報検索関数
def file_serch():
    i = 1
    folder_pass = entry.get()
    file_info = os.listdir(folder_pass)

    tk.Label(base_2, text='名前').grid(row=0, column=0)
    tk.Label(base_2, text='サイズ').grid(row=0, column=1)
    tk.Label(base_2, text='作成時刻').grid(row=0, column=2)
    tk.Label(base_2, text='最終アクセス時刻').grid(row=0, column=3)
    for file_name in file_info:
        file_size = os.path.getsize(folder_pass + '/' + file_name)
        tk.Label(base_2, text=file_name).grid(row=i, column=0)
        tk.Label(base_2, text=str(file_size) + 'バイト').grid(row=i, column=1)

        file_timestamp = os.path.getmtime(folder_pass + '/' + file_name)
        file_time1 = datetime.datetime.fromtimestamp(file_timestamp)
        file_time = file_time1.strftime('%Y-%m-%d(%a) %H:%M:%S')
        tk.Label(base_2, text=str(file_time)).grid(row=i, column=2)

        file_timestamp1 = os.path.getatime(folder_pass + '/' + file_name)
        file_time1 = datetime.datetime.fromtimestamp(file_timestamp1)
        file_time = file_time1.strftime('%Y-%m-%d(%a) %H:%M:%S')
        tk.Label(base_2, text=str(file_time)).grid(row=i, column=3)

        i += 1


#ボタン
button_f = tk.Button(base, text='情報を表示', command=file_serch).pack()

base.mainloop()
