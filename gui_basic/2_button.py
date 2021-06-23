from tkinter import *
# from PIL import Image

root = Tk()
root.title("RPA for SWPart")
root.geometry("640x480")    # 가로 * 세로

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# image = Image.open('gui_basic/img.png')
photo = PhotoImage(file='gui_basic/img.png')
btn6 = Button(root, image=photo, text="버튼6")
btn6.pack()

def btncmd():
    print("버튼 클릭")

btn7 = Button(root, text="버튼7", command=btncmd)
btn7.pack()

root.mainloop()