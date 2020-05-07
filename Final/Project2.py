from tkinter import *

state_dict ={'Alabama':'montgomery','Arizona':'phoenix','Alaska':'juneau','Arkansas':'little rock','California':'sacramento',
              'Colorado':'denver','Connecticut':'hartford','Delaware':'dover','Florida':'tallahassee','Georgia':'atlanta',
              'Hawaii':'honolulu','Idaho':'boise','Illinois':'springfield','Indiana':'indianapolis','Iowa':'des moines',
              'Kansas':'topeka','Kentucky':'frankfort','Louisiana':'baton rouge','Maine':'augusta','Maryland':'annapolis',
              'Massachusetts':'boston','Michigan':'lansing','Minnesota':'st. paul','Mississippi':'jackson','Missouri':'jefferson city',
              'Montana':'helena','Nebraska':'lincoln','Nevada':'carson city','New Hampshire':'concord','New Jersey':'trenton',
              'New Mexico':'santa fe','New York':'albany','North Carolina':'raleigh','North Dakota':'bismarck','Ohio':'columbus',
              'Oklahoma':'oklahoma city','Oregon':'salem','Pennsylvania':'harrisburg','Rhode Island':'providence','South Carolina':'columbia',
              'South Dakota':'pierre','Tennessee':'nashville','Texas':'austin','Utah':'salt lake city','Vermont':'montpelier',
              'Virginia':'richmond','Washington':'olympia','West Virginia':'charleston','Wisconsin':'madison','Wyoming':'cheyenne'}
def click():
    entered_text = text_entry.get()
    output.delete(0.0, END)
    try:
        answer = state_dict[entered_text]
    except:
        answer = 'check you spelling and try again!'
    output.insert(END, answer)



window = Tk()
window.title("States and Capitals")
window.geometry("710x700")
window.configure(background="black")

photo1 = PhotoImage(file="United.gif")
Label(window,image=photo1 ).place(x=0, y=0)

Label(window, text="What state do you want to know the capital of?",
      bg="black", fg="white").place(x=0, y=450)

text_entry = Entry(window, width=20, bg="white")
text_entry.place(x=0, y=475)

Button(window, text="Submit", width=6, command=click).place(x=200, y=475)

Label(window, text="Capital:", bg="black", fg="white").place(x=0, y=510)

output = Text(window, width=25,height=1, background="white", font="bold")
output.place(x=0, y=530)


window.mainloop()
