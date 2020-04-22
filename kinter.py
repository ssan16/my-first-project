from tkinter import *

from PIL import Image,ImageTk


window=Tk()
window.geometry("850x850")
window.title("Sam's Project")

image0=Image.open("Map.jpg")
photo=ImageTk.PhotoImage(image0)

lab=Label(image=photo)
lab.pack()


def printme():
    print("test 1,2,3")

def exitnow():
    exit()

label1= Label(window,text="Do you know all the States and Capitals?",font=("arial",20,"bold"))
label1.place(x=300,y=20)


button1=Button(window,text="start",width=12,fg='red',bg='blue',command=printme)
button1.place(x=160,y=500)

button2=Button(window,text="quit",width=12,fg='red',bg='blue',command=exitnow)
button2.place(x=160,y=550)


window.mainloop()
