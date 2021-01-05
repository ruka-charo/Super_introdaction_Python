#入力された日付の曜日を計算するソフト
import datetime
import tkinter as tk


#ウインドウの作成
base = tk.Tk()
base.geometry('300x250')

#ラベル表示
label = tk.Label(base, text='曜日を調べたい日付を入力してください。').pack()

label_y = tk.Label(base, text='年').pack()
entry_y = tk.Entry(base)
entry_y.insert(tk.END, '')
entry_y.pack()

label_m = tk.Label(base, text='月').pack()
entry_m = tk.Entry(base)
entry_m.insert(tk.END, '')
entry_m.pack()

label_d = tk.Label(base, text='日').pack()
entry_d = tk.Entry(base)
entry_d.insert(tk.END, '')
entry_d.pack()

#計算関数
def cal():
    y = int(entry_y.get())
    m = int(entry_m.get())
    d = int(entry_d.get())
    day = datetime.date(y, m, d)

    tk.Label(base, text=str(day) + '：' + day.strftime('%A')).pack()


#実行ボタン
button_cal = tk.Button(base, text='曜日を計算', command=cal).pack()

base.mainloop()
