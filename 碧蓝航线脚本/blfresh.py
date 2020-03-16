import win32con, win32api, win32gui
from time import sleep
from sys import argv
from random import randint
from blconf import *

def genpwm(point, wait):
    return [
        ['选择舰队', point, 1],
        ['确认出击', 选择舰队, 1],
        ['战斗中', 确认出击, wait],
        ['战斗结束', 战斗结算, 1],
        ['等待动画', 战斗结算, 2],
        ['等待潜艇', 战斗结算, 1],
        ['主界面', 战斗结算, 2]
    ]

def GetWindowPointSize(hwnd):
    x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
    return x1, y1, x2, y2, x2-x1, y2-y1

def flash(pw, title, ihwnd, times = 0):
    def click(points):
        p = tuple(map(int,points))
        win32api.SetCursorPos(p)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, *p, 0, 0)
        sleep(0.05 + randint(0,12) / randint(80,118))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, *p, 0, 0)
    def rf(x, y, width, height):
        for name, ppoints, wait in pw:
            points = (int(ppoints[0] * width / 100) + x, int(ppoints[1] * height / 100) + y)
            click(points)
            if wait > 0.1:
                for i in range(0,wait*10):
                    print('%s %d/%d (%.1f%%)        ' % (name, i/10, wait, (i/10 / wait) * 100), end='\r', flush=True)
                    sleep(0.1)
                print('%s %d/%d (%d%%)        ' % (name, wait, wait, 100), flush=True)
            else:
                sleep(wait)

    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        hwnd = ihwnd
    x1, y1, _, _, w, h = GetWindowPointSize(hwnd)
    print("切换焦点避免第一次点击失效......")
    click((0.5*w + x1, 0.5*h + y1))
    sleep(0.5)
    if times == 0:
        while True:
            rf(x1, y1, w, h)
    else:
        for ti in range(0,times):
            print('\n第%d遍，共%d遍(%.2f%%): ' % ( ti+1, times, (ti+1)/times * 100))
            rf(x1, y1, w, h)

def Check():
    for wft in range(1,51):
        print("请用5s的时间讲焦点切换到模拟器的窗口上(%.1f/5)" % (wft / 10), end='\r')
        sleep(0.1)
    print()
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    x1, y1, x2, y2, w, h = GetWindowPointSize(hwnd)
    print("你的焦点现在在窗口：”%s“(%d)上" %(title, hwnd))
    print("窗口位置：(%d, %d)" % (x1, y1), "大小：(%d, %d)" % (w, h))
    print("请将焦点切回程序，按回车显示当前鼠标位置信息", end='')
    try:
        while True:
            input()
            mx, my = win32api.GetCursorPos()
            if (mx<x1 or mx >x2) and (my<y1 or my>y2):
                print("你现在鼠标在窗口外", end='')
            else:
                print("你现在鼠标位置百分比是：(%.2f, %.2f)" % (((mx-x1)/w)*100, ((my-y1)/h)*100), end='')
    except KeyboardInterrupt:
        pass

if len(argv) == 3:
    imode = argv[1]
    ftime = argv[2]
elif len(argv) == 2:
    imode = argv[1]
    if imode.lower() == "check":
        Check()
        exit(0)
    ftime = input('次数: ')
else:
    imode = input('难度(%s): ' % ', '.join(mode.keys()))
    ftime = input('次数: ')

flash(genpwm(**mode.get(imode, None)), 窗口标题, 窗口句柄, int(ftime) if ftime.isnumeric() else 0)
#python blfresh.py check
#blfresh.py (难度) (次数) (这里需要管理员权限，用于win32api.mouse_event)
#刷困难： python blfresh.py Hard 15
#刷普通： python blfresh.py Normal 15
#刷简单： python blfresh.py Easy 15
