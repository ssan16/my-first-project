from tkinter import *
from random import randint



def click():
    entered_text = text_entry.get()


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
    randomNum = randint(0,len(states)-1)
    subbox.config(text = "what is the capital of"+" "+ states[randomNum][0])
    
def gui():

    global subbox,text_entry
    sub= Tk()
    sub.title("Sam's Project")
    sub.geometry("500x500")

    topframe=Frame(sub,bg= "black")
    topframe.place(relwidth=1,relheight = 0.07)

    Label(topframe,text="States and Capitals",anchor = CENTER).place(x=10,y=5)
    
    score = Label(topframe,text = "Score=0",anchor = CENTER)
    score.place(x=420, y=5)

    subbox=Label(sub,bg = "pink",font=18)
    subbox.place(relx = 0.1,rely= 0.2, relwidth= 0.8, relheight = 0.3)

    start_butt= Button(sub, text=" Next ",command =showq)
    start_butt.place(x=350,y=470)


    text_entry = Entry(sub, width=20, font="bold")
    text_entry .place(x=150, y=345)

    submit_butt= Button(sub, text="Submit", width=6, command= click) . place(x=350,y=350)


    sub.mainloop()

gui()
qgroup()
showq()
click()
