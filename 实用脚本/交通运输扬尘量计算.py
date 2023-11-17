import tkinter as tk

def calculate_dust():
    V = float(entry_V.get())
    M = float(entry_M.get())
    P = float(entry_P.get())
    L = float(entry_L.get())
    Q = float(entry_Q.get())
    Qp = 0.123*(V/5)*((M/6.8)**0.85)*((P/0.5)**0.72)
    Qpp = Qp*L*Q/M
    label_result.config(text=f"交通运输起尘量为: {Qp}kg/km辆\n"
                             f"运输途中起尘量为：{Qpp}kg/a")

# 创建窗口
window = tk.Tk()
window.title("车辆运输途中起尘量计算器")

# 创建输入框和标签
label_Qp = tk.Label(window, text="参考公式为：Qp=0.123(V/5)*((M/6.8)**0.85)*(P/0.5)**0.72")
label_Qp.pack()
label_Qpp = tk.Label(window, text="参考公式为：Q'p=Qp*L*Q/M")
label_Qpp.pack()
label_V = tk.Label(window, text="车辆行驶速度，km/h：（V）")
label_V.pack()
entry_V = tk.Entry(window)
entry_V.pack()

label_M = tk.Label(window, text="车辆载重，t/辆：（M）")
label_M.pack()
entry_M = tk.Entry(window)
entry_M.pack()

label_P = tk.Label(window, text="路面状况，以每米2路面灰尘覆盖率表示，kg/㎡：（P）")
label_P.pack()
entry_P = tk.Entry(window)
entry_P.pack()

label_L = tk.Label(window, text="运输距离，km：（L）")
label_L.pack()
entry_L = tk.Entry(window)
entry_L.pack()

label_Q = tk.Label(window, text="运输量，t/a：（Q）")
label_Q.pack()
entry_Q = tk.Entry(window)
entry_Q.pack()
# 创建计算按钮
button_calculate = tk.Button(window, text="计算", command=calculate_dust)
button_calculate.pack()
# 创建结果标签
label_result = tk.Label(window, text="车辆运输途中的起尘量为: ")
label_result.pack()

# 进入消息循环
window.mainloop()