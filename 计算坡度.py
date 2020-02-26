import math
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
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
def calculate():
    b1 = tk.Button(window, text='计算', width=10,
                   height=2, command=insert_point, font=('Arial', 12))
    b1.pack()
t = tk.Text(window, height=4, font=('Arial', 18))
t.pack()
calculate()
window.mainloop()