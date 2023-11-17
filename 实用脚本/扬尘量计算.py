import tkinter as tk

def calculate_dust():
    V50 = float(entry_v50.get())
    V0 = float(entry_v0.get())
    W = float(entry_w.get())
    Q = 2.1 * (V50 - V0) ** (3 * 10 ** (-1.023 * W))
    label_result.config(text=f"扬尘量为: {Q}KG/吨·年")

# 创建窗口
window = tk.Tk()
window.title("扬尘量计算器")

# 创建输入框和标签
label_Q = tk.Label(window, text="参考公式为：Q=2.1（V50–V0）3e-1.023W")
label_Q.pack()
label_v50 = tk.Label(window, text="距地面50米处的风速（m/s）：（V50）")
label_v50.pack()
entry_v50 = tk.Entry(window)
entry_v50.pack()

label_v0 = tk.Label(window, text="起尘风速（m/s）：（V0）")
label_v0.pack()
entry_v0 = tk.Entry(window)
entry_v0.pack()

label_w = tk.Label(window, text="尘粒含水率（%）：（W）")
label_w.pack()
entry_w = tk.Entry(window)
entry_w.pack()

# 创建计算按钮
button_calculate = tk.Button(window, text="计算", command=calculate_dust)
button_calculate.pack()

# 创建结果标签
label_result = tk.Label(window, text="扬尘量为: ")
label_result.pack()

# 进入消息循环
window.mainloop()