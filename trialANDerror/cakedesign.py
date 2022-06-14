import tkinter
from tkinter import *
from tkinter.colorchooser import *
from PIL import Image, ImageTk, ImageGrab
import os

def paint(event):
    x1, y1 = event.x - 1, event.y - 1
    x2, y2 = event.x + 1, event.y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color, width=pen_size)

def getColor():
    global pen_color
    color = askcolor()
    pen_color = color[1]

def size_up():
    global pen_size
    pen_size += 1

def size_down():
    global pen_size
    if pen_size > 1:
        pen_size -= 1

def erase():
    global pen_color
    pen_color="white"
    for i in range (0,6):
        size_up()

def getimage(event):
    global img1
    x1, y1 = event.x - 1, event.y - 1
    img1 = ImageTk.PhotoImage(Image.open("D:/충북대/2-1/오픈소스기초프로젝트/프로젝트/whip2.gif"))
    canvas.create_image(x1, y1, image=img1)

def save():
    box = (0, 0, 1250, 900)
    img = ImageGrab.grab(box)
    saveas='capture.png'
    img.save(saveas)


pen_color = "black"
pen_size = 1

if __name__=="__main__":
    window = Tk()
    window.title("케이크 장식하기")
    canvas = Canvas(window, width=1000, height=900)
    canvas.pack()
    canvas.bind("<B1-Motion>", paint)

    canvas.create_oval(300,50,700,450,fill="white")
    #canvas.create_rectangle(80,500,480,650,fill="white")
    #canvas.create_text(280,575,text="left")

    #canvas.create_rectangle(500, 500, 900, 650, fill="white")
    #canvas.create_text(700, 575, text="right")

    button_c = Button(window, text = "색 선택", width = 5, bg = "white", command = getColor, font = ("나눔바른펜", 12))
    button_c.place(x=0, y=0)

    button_w = Button(window, text="지우개", width=5, bg="white", command=lambda: erase(), font=("나눔바른펜", 12))
    button_w.place(x=0, y=40)

    button_img = Button(window, text="이미지", width=5, command= getimage, font=("나눔바른펜", 12))
    canvas.bind("<Button-3>", getimage)
    button_img.place(x=0, y=80)

    button_size_up = Button(window, text="굵게", command=size_up, width=5, font=("나눔바른펜", 12))
    button_size_up.place(x=0, y=120)

    button_size_down = Button(window, text="가늘게", command=size_down, width=5, font=("나눔바른펜", 12))
    button_size_down.place(x=0, y=160)

    button_text = Button(window, text="텍스트", width=5, font=("나눔바른펜", 12))
    button_text.place(x=0, y=200)

    button_save = Button(window, text="저장", width=5, fg="red", command=save, font=("나눔바른펜", 12))
    button_save.place(x=0, y=240)

    window.mainloop()
