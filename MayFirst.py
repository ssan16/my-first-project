from tkinter import *
from random import randint

count=0


def qgroup():
    states = [['Alabama','montgomery'],['Arizona','phoenix'],['Alaska','juneau'],['Arkansas','little rock'],['California','sacramento'],
              ['Colorado','denver'], ['Connecticut', 'hartford'],['Delaware','dover'],['Florida','tallahassee'],['Georgia','atlanta'],
              ['Hawaii','honolulu'],['Idaho', 'boise'],['Illinois','springfield'], ['Indiana', 'indianapolis'],['Iowa','des moines'],
              ['Kansas','topeka'],['Kentucky','frankfort'],['Louisiana', 'baton rouge'],['Maine','augusta'],['Maryland', 'annapolis'],
              ['Massachusetts','boston'],['Michigan','lansing'],['Minnesota','st. paul'],['Mississippi','jackson'],['Missouri','jefferson city'],
              ['Montana','helena'],['Nebraska','lincoln'],['Nevada','carson city'],['New Hampshire','concord'],['New Jersey','trenton'],
              ['New Mexico','santa fe'],['New York','albany'],['North Carolina','raleigh'],['North Dakota','bismarck'],['Ohio','columbus'],
              ['Oklahoma','oklahoma city'],['Oregon','salem'],['Pennsylvania','harrisburg'],['Rhode Island','providence'],['South Carolina','columbia'],
              ['South Dakota', 'pierre'], ['Tennessee','nashville'],['Texas','austin'],['Utah','salt lake city'],['Vermont','montpelier'],
              ['Virginia','richmond'],['Washington','olympia'],['West Virginia','charleston'],['Wisconsin','madison'],['Wyoming','cheyenne']]

    for state in states:
        return states


def showq():
    states=qgroup()
    global count
    count +=1
    randomNum = randint(0,len(states)-1)
    topbox.config(text=" Question={0}".format(count))
    subbox.config(text = "what is the capital of"+" "+ states[randomNum][0])
    entry.config(text=states[randomNum][1])
    

#function for GUI
def box():

    global subbox,topbox,entry
    sub= Tk()
    sub.title("Sam's Project")
    sub.geometry("500x500")

    an=StringVar()

    topframe=Frame(sub,bg= "#3285a8")
    topframe.place(relwidth=1,relheight = 0.07)

    Label(topframe,text="States and Capitals",anchor = CENTER).place(x=10,y=5)
    #score added to top right hand corner
    score = Label(topframe,text = "Score=0",anchor = CENTER)
    score.place(x=420, y=5)

    topbox=Label(sub,bg ="#3285a8")
    topbox.place(relx=0.1,rely = 0.1, relwidth = 0.8, relheight =0.1)
    #where the question will be
    subbox=Label(sub,bg = "#cfbccb")
    subbox.place(relx = 0.1,rely= 0.2, relwidth= 0.8, relheight = 0.3)
    #function to hide begin button and start question
    def hidestart():
        startbut.destroy()
        showq()

    startbut = Button(sub, text = "Begin",fg="#3285a8",command = hidestart)
    startbut.place(relx = 0.1,rely= 0.6,relwidth=0.8,relheight = 0.3)

    doneb= Button(sub, text="Next!",command =showq)
    doneb.place(x=405,y=470)

    answer= Label(sub,text = "Answer:", width=20, font="bold")
    answer.place(x=40, y=345)    
    entry = Entry(sub,textvar=an)
    entry.place(x=175,y=342)

    


    sub.mainloop()

box()
qgroup()
showq()
