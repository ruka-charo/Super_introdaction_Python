#生きた日数を計算するソフト
import datetime
import tkinter as tk
import tkinter.messagebox as msg

#ウィンドウの作成
base = tk.Tk()


#日数計算の関数
def cal_day():
    birthday = datetime.date(1996,1,20)
    today = datetime.date.today()
    life = today - birthday
    print('生きた日数は', life, 'です。')

    base.withdraw()
    response = msg.showinfo('計算結果', str(life))


#ボタン
button = tk.Button(base, text='生きた日数を算出', command=cal_day).pack()


base.mainloop()
