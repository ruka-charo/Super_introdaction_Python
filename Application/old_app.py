#誕生日 ⇄ 年齢 を計算するソフト
import datetime
import tkinter as tk

#準備
today = datetime.date.today()
today_y = today.year
today_m = today.month
today_d = today.day

#ウインドウの作成
base = tk.Tk()
base.geometry('480x300')


#ラベル表示
label_1 =tk.Label(base, text='【年齢計算】') .grid(row=0, column=1)
label_2 = tk.Label(base, text='誕生日を入力してください。').grid(row=1, column=0)

label_y = tk.Label(base, text='年').grid(row=2, column=0)
entry_y = tk.Entry(base)
entry_y.insert(tk.END, '')
entry_y.grid(row=3, column=0)

label_m = tk.Label(base, text='月').grid(row=4, column=0)
entry_m = tk.Entry(base)
entry_m.insert(tk.END, '')
entry_m.grid(row=5, column=0)

label_d = tk.Label(base, text='日').grid(row=6, column=0)
entry_d = tk.Entry(base)
entry_d.insert(tk.END, '')
entry_d.grid(row=7, column=0)

label_3 = tk.Label(base, text='指定日を入力してください。\n(デフォルト=今日)')\
.grid(row=1, column=2)

label_y2 = tk.Label(base, text='年').grid(row=2, column=2)
entry_y2 = tk.Entry(base)
entry_y2.insert(tk.END, today_y)
entry_y2.grid(row=3, column=2)

label_m2 = tk.Label(base, text='月').grid(row=4, column=2)
entry_m2 = tk.Entry(base)
entry_m2.insert(tk.END, today_m)
entry_m2.grid(row=5, column=2)

label_d2 = tk.Label(base, text='日').grid(row=6, column=2)
entry_d2 = tk.Entry(base)
entry_d2.insert(tk.END, today_d)
entry_d2.grid(row=7, column=2)


#計算関数
def cal1():
    y = int(entry_y.get())
    m = int(entry_m.get())
    d = int(entry_d.get())

    y2 = int(entry_y2.get())
    m2 = int(entry_m2.get())
    d2 = int(entry_d2.get())

    birthday = datetime.date(y, m, d)
    sel_day = datetime.date(y2, m2, d2)

    if sel_day.month > birthday.month:
        old = sel_day.year - birthday.year
        tk.Label(base, text=' ' + str(sel_day) + '\n' + str(old) + '才です。')\
        .grid(row=9, column=1)

    elif sel_day.month < birthday.month:
        old = sel_day.year - birthday.year - 1
        tk.Label(base, text=' ' + str(sel_day) + '\n' + str(old) + '才です。')\
        .grid(row=9, column=1)

    elif sel_day.month == birthday.month:
        if sel_day.day >= birthday.day:
            old = sel_day.year - birthday.year
            tk.Label(base, text=' ' + str(sel_day) + '\n' + str(old) + '才です。')\
            .grid(row=9, column=1)

        elif sel_day.day < birthday.day:
            old = sel_day.year - birthday.year - 1
            tk.Label(base, text=' ' + str(sel_day) + '\n' + str(old) + '才です。')\
            .grid(row=9, column=1)

#実行ボタン
button_cal1 = tk.Button(base, text='年齢を計算', command=cal1).grid(row=8, column=1)


base.mainloop()
