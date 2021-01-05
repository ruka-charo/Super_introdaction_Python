#%%ボタンの配置１
import tkinter as tk

base = tk.Tk()

button_1 = tk.Button(base, text='push1!')
button_2 = tk.Button(base, text='push2!')
button_3 = tk.Button(base, text='push3!')
button_1.pack()
button_2.pack(side=tk.LEFT)
button_3.pack(side=tk.RIGHT)

base.mainloop()

#%%ボタンの配置2
import tkinter as tk

base = tk.Tk()

button_1 = tk.Button(base, text='push1!')
button_2 = tk.Button(base, text='push2!')
button_3 = tk.Button(base, text='push3!')
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=1, column=1)

base.mainloop()

#%%ボタンの配置3
import tkinter as tk

base = tk.Tk()

button_1 = tk.Button(base, text='push1!')
button_2 = tk.Button(base, text='push2!')
button_3 = tk.Button(base, text='push3!')
button_1.place(x=0, y=0)
button_2.place(x=50, y=30)
button_3.place(x=100, y=60)

base.mainloop()

#%%ボタンを押した時の挙動
import tkinter　as tk

base = tk.Tk()

def push():
    print('MELON!')

button = tk.Button(base, text='push', command=push)
button.pack()

base.mainloop()

#%%ラベル
import tkinter as tk

base = tk.Tk()
tk.Label(base, text='赤', bg='red', width=20).pack()
tk.Label(base, text='青', bg='blue', width=20).pack()
tk.Label(base, text='緑', bg='green', width=20).pack()

base.mainloop()

#%%チェックボックス
import tkinter as tk

base = tk.Tk()
topping = {0:'のり', 1:'煮玉子', 2:'もやし', 3:'チャーシュー'}
check_value = {}

for i in range(len(topping)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(base, variable=check_value[i], text=topping[i]).pack(anchor=tk.W)

def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(topping[i])

tk.Button(base, text='注文', command=buy).pack()

base.mainloop()

#%%ラジオボタン
import tkinter as tk

base = tk.Tk()
radio_value = tk.IntVar()
radio_value.set(1)

lunch = {0:'Aランチ', 1:'Bランチ', 2:'Cランチ'}

tk.Radiobutton(base, text=lunch[0], variable=radio_value, value=0).pack()
tk.Radiobutton(base, text=lunch[1], variable=radio_value, value=1).pack()
tk.Radiobutton(base, text=lunch[2], variable=radio_value, value=2).pack()

def buy():
    value = radio_value.get()
    print(lunch[value])

tk.Button(base, text='注文', command=buy).pack()

base.mainloop()

#%%メッセージボックス
import tkinter as tk
import tkinter.messagebox as msg

base = tk.Tk()
base.withdraw()
''
response = msg.askyesno('大変！！', '大丈夫ですか？')
if(response==True):
    print('大丈夫')
else:
    print('ダメ')

base.mainloop()

#%%メッセージ入力
import tkinter as tk

base = tk.Tk()
string = tk.StringVar()
entry = tk.Entry(base, textvariable=string).pack()
label = tk.Label(base, textvariable=string).pack()

base.mainloop()

#%%メニュー
import tkinter as tk

base = tk.Tk()

def supermode():
    print('super mode!')

menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
filemenu.add_command(label='supermode', command=supermode)
menubar.add_cascade(label='Operation', menu=filemenu)
base.config(menu=menubar)

base.mainloop()

#%%メニュー2
import tkinter as tk
import tkinter.filedialog as fd

base = tk.Tk()

def open():
    filename = fd.askopenfilename()
    print('open file => ' + filename)

def exit():
    base.destroy()

def find():
    print('find!')

menubar = tk.Menu(base)


filemenu = tk.Menu(menubar)
#メニューバーに「File」の項目を作成
menubar.add_cascade(label='File', menu=filemenu)
#「File」項目内にコマンドを作成
filemenu.add_command(label='open', command=open)
filemenu.add_command(label='exit', command=exit)


editmenu = tk.Menu(menubar)
#メニューバーに「Edit」の項目を作成
menubar.add_cascade(label='Edit', menu=editmenu)
#「Edit」項目内にコマンドを作成
editmenu.add_command(label='find', command=find)

#baseに上記ニューバーを設置
base.config(menu=menubar)

base.mainloop()
