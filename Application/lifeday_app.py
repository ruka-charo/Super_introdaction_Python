#入力された誕生日から、生きた日数を計算するソフト
import datetime
import tkinter as tk


#ウィンドウの作成
base = tk.Tk()
base.geometry('300x250')


#誕生日の入力
string = tk.StringVar()

label_n = tk.Label(base, text='誕生日を入力してください。').pack()

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


#日数計算の関数
def cal_day():
    year = int(entry_y.get())
    month = int(entry_m.get())
    day = int(entry_d.get())

    birthday = datetime.date(year,month,day)
    today = datetime.date.today()
    life = today - birthday

    tk.Label(base, text='生きた日数は' + str(life) + 'です。').pack()


#ボタン
button_cal = tk.Button(base, text='生きた日数を算出', command=cal_day).pack()

base.mainloop()
