#年号 ⇄ 西暦　の変換ソフト
import datetime
import tkinter as tk

#準備
base = tk.Tk()
base.geometry('400x300')

radio_value = tk.IntVar()
radio_value.set(1)
year_name = {0:'大正', 1:'昭和', 2:'平成', 3:'令和'}
year_dis = [1912, 1926, 1989, 2019]


#条件設定：ボタン作成
string = tk.StringVar()
label_y = tk.Label(base, text='【西暦換算】')
label_y.grid(row=0, column=0)

for i in range(len(year_name)):
    tk.Radiobutton(base, text=year_name[i], variable=radio_value, value=i)\
.grid(row=i+1, column=0)

label_y1 = tk.Label(base, text='年を入力')
label_y1.grid(row=len(year_name)+1, column=0)
entry_y1 = tk.Entry(base)
entry_y1.insert(tk.END, '')
entry_y1.grid(row=len(year_name)+2, column=0)

label_yy = tk.Label(base, text='【年号換算】')
label_yy.grid(row=0, column=4)
label_y2 = tk.Label(base, text='年を入力')
label_y2.grid(row=len(year_name)+1, column=4)
entry_y2 = tk.Entry(base)
entry_y2.insert(tk.END, '')
entry_y2.grid(row=len(year_name)+2, column=4)

#年号計算関数
def cal():
    year_num = int(entry_y1.get())
    value_num = radio_value.get()

    for i in range(len(year_name)):
        if value_num == i:
            if year_num == 1:
                tk.Label(base, text='  ' + year_name[i] + '元年は、\
西暦'+ str(year_dis[i]) + '年です。').grid(row=len(year_name)+4, column=0)
            else:
                year_cal = year_dis[i] + year_num - 1
                tk.Label(base, text='  ' + year_name[i] + str(year_num) + '年は、\
西暦' + str(year_cal) + '年です。').grid(row=len(year_name)+4, column=0)

def cal_2():
    year_num2 = int(entry_y2.get())

    for i in range(len(year_name)):
        if i <= len(year_name) - 2:
            if year_dis[i] < year_num2 < year_dis[i+1]:
                year_cal2 = year_num2 - year_dis[i] + 1
                tk.Label(base, text='西暦' + str(year_num2) + '年は、' + \
year_name[i] + str(year_cal2) + '年です。').grid(row=len(year_name)+4, column=4)

            elif year_num2 == year_dis[i]:
                tk.Label(base, text='西暦' + str(year_num2) + '年は、' + \
year_name[i] + '元年です。').grid(row=len(year_name)+4, column=4)

        elif i == len(year_name) - 1:
            if year_dis[i] < year_num2:
                year_cal2 = year_num2 - year_dis[i] + 1
                tk.Label(base, text='西暦' + str(year_num2) + '年は、' + \
year_name[i] + str(year_cal2) + '年です。').grid(row=len(year_name)+4, column=4)

            elif year_num2 == year_dis[i]:
                tk.Label(base, text='西暦' + str(year_num2) + '年は、' + \
year_name[i] + '元年です。').grid(row=len(year_name)+4, column=4)

    if year_num2 < year_dis[0]:
        tk.Label(base, text='西暦' + str(year_num2) + '年は、' + \
year_name[0] + '以前です。').grid(row=len(year_name)+4, column=4)


#計算実行ボタン
tk.Button(base, text='西暦に変換', command=cal).grid(row=len(year_name)+3, column=0)
tk.Button(base, text='年号に変換', command=cal_2).grid(row=len(year_name)+3, column=4)

base.mainloop()
