from tkinter import *



    
root = Tk()   #making our root window 'root'

x = StringVar()
x.set(0.00)

w = StringVar()
w.set(100.00)

e = StringVar()
e.set("")

def add():
    global x
    global w
    try:
        a = float(gradeEntry.get())
        b = float(weightEntry.get()) / 100
        if ( (b*100) > float(w.get())):
            e.set("Error: That is over 100 total weight!")
        elif (a<100) and (b<1):
            c = round((float(x.get()) + a*b ), 2)
            x.set(c)
            d = round((float(w.get()) - (b*100)), 2)
            w.set(d)
            e.set("")
        else:
            e.set("Error: Please enter integers from 0-100!z")
        
    except:
        e.set("Error: Please enter integers from 0-100!")

def sub():
    global x
    global w
    try:
        a = float(gradeEntry.get())
        b = float(weightEntry.get()) / 100
        if (( (b*100) + float(w.get())) > 100):
            e.set("Error: That is over 100 total weight!")
        elif (a<100) and (b<1):
            c = round((float(x.get()) - a*b ), 2)
            x.set(c)
            d = round((float(w.get()) + (b*100)), 2)
            w.set(d)
            e.set("")
        else:
            e.set("Error: Please enter integers from 0-100!")
        
    except:
        e.set("Error: Please enter integers from 0-100!")


##def calc():
##    global x
##    global w
##    try:
##        a = float(wantEntry.get())
##        if (a > 100):
##            e2.set("Error: Please enter an integer from 0-100!")
        

def zero():
    global x
    global w
    x.set(0.00)
    w.set(100.00)
    e.set("")


errorLabel = Label(root, textvariable = e, font=("default", 10), fg = "red")
errorLabel.place(x=25, y=15, height=20, width=300)



gradeEntry = Entry(root)
gradeEntry.place(x=60, y=50, height=25, width=100)
gradeLabel = Label(root, text="Grade (0-100)")
gradeLabel.place(x=60, y=85, height=25, width=100)

weightEntry = Entry(root)
weightEntry.place(x=190, y=50, height=25, width=100)
weightLabel = Label(root, text="Weight (0-100)")
weightLabel.place(x=190, y=85, height=25, width=100)



calcButton = Button(root, text = "Add to grade", command = add)
calcButton.place(x=350, y=20, height=25, width=150)

subButton = Button(root, text = "Subtract from grade", command = sub)
subButton.place(x=350, y=55, height=25, width=150)

zeroButton = Button(root, text = "Reset", command = zero)
zeroButton.place(x=350, y=90, height=25, width=150)



##wantEntry = Entry(root)
##wantEntry.place(x=550, y=50, height=25, width=150)
##gradeLabel = Label(root, text="Grade Wanted (0-100)")
##gradeLabel.place(x=550, y=85, height=25, width=150)
##
##wantButton = Button(root, text = "Calculate", command = calc)
##wantButton.place(x=350, y=20, height=25, width=150)



yourGradeLabel = Label(root, text="Your grade:", font=("default", 15))
yourGradeLabel.place(x=20, y=150, height=25, width=200)

yourGradeValLabel = Label(root, textvariable=x, font=("default", 15))
yourGradeValLabel.place(x=220, y=150, height=25, width=100)



weightRemLabel = Label(root, text="Weight remaining:", font=("default", 15))
weightRemLabel.place(x=20, y=180, height=25, width=200)

weightRemValLabel = Label(root, textvariable=w, font=("default", 15))
weightRemValLabel.place(x=220, y=180, height=25, width=100)




root.mainloop() #runs main root window
