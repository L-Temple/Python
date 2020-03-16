import math
import tkinter as tk
import re
window = tk.Tk()
window.title('My Window')
window.geometry('600x600')
l1 = tk.Label(window, text='高度', font=('Arial', 12))
l2 = tk.Label(window, text='长度', font=('Arial', 12))
l3 = tk.Label(window, text='坡度', font=('Arial', 12))
e1 = tk.Entry(window, show=None, font=('Arial', 12))  # 显示成明文形式
e2 = tk.Entry(window, show=None, font=('Arial', 12))  # 显示成明文形式
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
def insert_point():  # 在鼠标焦点处插入输入内容
    t.delete(1.0, tk.END)
    var1 = int(e1.get())
    var2 = int(e2.get())
    c = math.sqrt(var1*var1+var2*var2)
    rad = math.asin(var1/c)
    content = rad*(180/math.pi)
    minute = (content-int(content))*60
    second = (minute-int(minute))*60
    contents = str(int(content))+str('°')+str(int(minute))+str("'")+str(int(second))+str("''")
    t.insert('insert', content)
    t.insert('end', '\n')
    t.insert('end', contents)
def conversion1():
    t1.delete(1.0, tk.END)
    var1 = int(e4.get())
    var2 = int(e5.get())
    var3 = int(e6.get())
    second = var3/3600
    minute = var2/60
    content = float(var1)+float(minute)+float(second)
    t1.insert('insert', content)
def conversion2():
    t1.delete(1.0, tk.END)
    var2 = float(e3.get())
    content = var2
    minute = (content-int(content))*60
    second = (minute-int(minute))*60
    contents = str(int(content))+str('°')+str(int(minute))+str("'")+str(int(second))+str("''")
    t1.insert('insert', contents)
def calculate():
    b1 = tk.Button(window, text='计算', width=10,
                   height=2, command=insert_point, font=('Arial', 12))
    b1.pack()
def change1():
    b2 = tk.Button(window, text='转换成度数', width=10,
                   height=2, command=conversion1, font=('Arial', 12))
    b2.place(x=100, y=525, anchor='nw')
def change2():
    b3 = tk.Button(window, text='转换成度分秒', width=10,
                   height=2, command=conversion2, font=('Arial', 12))
    b3.place(x=400, y=525, anchor='nw')
t = tk.Text(window, height=4, font=('Arial', 18))
e3 = tk.Entry(window, show=None, font=('Arial', 12))
e4 = tk.Entry(window, show=None, font=('Arial', 12))
e5 = tk.Entry(window, show=None, font=('Arial', 12))
e6 = tk.Entry(window, show=None, font=('Arial', 12))
l4 = tk.Label(window, text='度数', font=('Arial', 12))
l5 = tk.Label(window, text='度分秒', font=('Arial', 12))
t1 = tk.Text(window, height=4, font=('Arial', 18))
t.pack()
calculate()
l4.pack()
e3.pack()
l5.pack()
e4.pack()
e5.pack()
e6.pack()
t1.pack()
change1()
change2()
window.mainloop()