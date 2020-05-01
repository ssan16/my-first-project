from tkinter import *

def box():

    sub= Tk()
    sub.title("Sam's Project")
    sub.geometry("500x500")

    topframe=Frame(sub,bg= "#3285a8")
    topframe.place(relwidth=1,relheight = 0.07)

    Label(topframe,text="States and Capitals",anchor = CENTER).place(x=10,y=5)

    score = Label(topframe,text = "Score=0",anchor = CENTER)
    score.place(x=420, y=5)

    subbox=Label(sub,bg = "#cfbccb")
    subbox.place(relx = 0.1,rely= 0.2, relwidth= 0.8, relheight = 0.3)

    doneb= Button(sub, text="next state=>")
    doneb.place(x=405,y=470)

    option1 = Button(sub,text= "test")
    option1.place(relx = 0.1,rely = 0.6, relwidth = 0.35,relheight = 0.1)

    option2 = Button(sub,text= "test")
    option2.place(relx = 0.55,rely = 0.6, relwidth = 0.35,relheight = 0.1)

    option3 = Button(sub,text= "test")
    option3.place(relx = 0.1,rely = 0.8, relwidth = 0.35,relheight = 0.1)

    option4 = Button(sub,text= "test")
    option4.place(relx = 0.55,rely = 0.8, relwidth = 0.35,relheight = 0.1)

    sub.mainloop()

box()
