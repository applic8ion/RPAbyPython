import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("RPA for SWPart")
root.geometry("640x480")    # 가로 * 세로


# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")  # 종료 시점을 모를 때 좌우로 왔다갔다
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10)     # 값 지정 시 10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop()  # 작동 중지

btn = Button(root, text="중지", command=btncmd)
btn.pack()

# progressbar2
p_var2 = DoubleVar()    # 실수 반영을 위해 Double
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 10ms delay
        p_var2.set(i)       # progressbar 값 설정
        progressbar2.update()   # GUI update
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()