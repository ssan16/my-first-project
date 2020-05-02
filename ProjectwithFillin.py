from tkinter import *



def qgroup():
    states = [['Alabama','Montgomery'],['Arizona','Phoenix'],['Alaska','Juneau'],['Arkansas','Little Rock'], ['California', 'Sacramento'], ['Colorado', 'Denver'], ['Connecticut', 'Hartford'], ['Delaware', 'Dover'],['Florida', 'Tallahassee'], ['Georgia', 'Atlanta'], ['Hawaii', 'Honolulu'],['Idaho', 'Boise'],['Illinois', 'Springfield'], ['Indiana', 'Indianapolis'],['Iowa','Des Moines'],['Kansas', 'Topeka'],['Kentucky', 'Frankfort'],['Louisiana', 'Baton Rouge'],['Maine', 'Augusta'],['Maryland', 'Annapolis'],['Massachusetts', 'Boston'],['Michigan','Lansing'],['Minnesota','St. Paul'],['Mississippi','Jackson'],['Missouri','Jefferson city'],['Montana','Helena'],['Nebraska','Lincoln'],['Nevada','Carson City'],['New Hampshire','Concord'],['New Jersey','Trenton'],['New Mexico','Santa Fe'],['New York', 'Albany'],['North Carolina', 'Raleigh'],['North Dakota','Bismarck'],['Ohio','Columbus'],['Oklahoma','Oklahoma City'],['Oregon', 'Salem'],['Pennsylvania','Harrisburg'],['Rhode Island','Providence'],['South Carolina','Columbia'],['South Dakota', 'Pierre'], ['Tennessee', 'Nashville'],['Texas','Austin'],['Utah', 'Salt Lake City'],['Vermont', 'Montpelier'],['Virginia','Richmond'],['Washington','Olympia'],['West Virginia', 'Charleston'],['Wisconsin', 'Madison'],['Wyoming','Cheyenne']]

    for state in states:

        return states
#show question
def showq():
    states= qgroup()
    subbox.config(text = states[0][0])

#function for GUI
def box():

    global subbox 
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

    topbox=Label(sub,text= "what is the capital of?",bg ="#3285a8")
    topbox.place(relx=0.1,rely = 0.1, relwidth = 0.8, relheight =0.1)
    #where the question will be
    subbox=Label(sub,bg = "#cfbccb")
    subbox.place(relx = 0.1,rely= 0.2, relwidth= 0.8, relheight = 0.3)
    #function to hide st
    def hidestart():
        startbut.destroy()
        showq()

    startbut = Button(sub, text = "Begin", command = hidestart)
    startbut.place(x=5,y = 50)

    doneb= Button(sub, text="Next!")
    doneb.place(x=405,y=470)

    answer= Label(sub,text = "Answer:", width=20, font="bold")
    answer.place(x=40, y=345)    
    entry = Entry(sub,textvar=an)
    entry.place(x=175,y=342)


    sub.mainloop()

box()
qgroup()
showq()
