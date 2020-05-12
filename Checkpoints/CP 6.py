from tkinter import *



    
root = Tk()   #making our root window 'root'

x = StringVar()
x.set(0.00)

w = StringVar()
w.set(100.00)

e = StringVar()
e.set("")

e2 = StringVar()
e2.set("")

n = StringVar()
n.set("")

def add():
    print("a7a")
    try:
        a = float(gradeEntry.get())
        b = float(weightEntry.get()) / 100
        if ( (b*100) > float(w.get())):
            e.set("Error: That is over 100 total weight!")
        elif (a<100) and (b<1):
            c = round((float(x.get()) + a*b ), 2)
            if c < 0:
                e.set("Error: That is under 100 total grade!")
            else:
                x.set(c)
                d = round((float(w.get()) - (b*100)), 2)
                w.set(d)
                e.set("")
        else:
            e.set("Error: Please enter integers from 0-100!z")
        
    except:
        e.set("Error: Please enter integers from 0-100!")

def sub():
    try:
        a = float(gradeEntry.get())
        b = float(weightEntry.get()) / 100
        if (( (b*100) + float(w.get())) > 100):
            e.set("Error: That is over 100 total weight!")
        elif (a<100) and (b<1):
            c = round((float(x.get()) - a*b ), 2)
            if c < 0:
                e.set("Error: That is under 100 total grade!")
            else:
                x.set(c)
                d = round((float(w.get()) + (b*100)), 2)
                w.set(d)
                e.set("")
        else:
            e.set("Error: Please enter integers from 0-100!")
        
    except:
        e.set("Error: Please enter integers from 0-100!")


def calc():
    try:
        a = float(wantEntry.get())
        if (a > 100) or (a < 0):
            e2.set("Error: Please enter an dsasdinteger from 0-100!")
        else:
            b = (a - x)
            c = round((b/w), 2)
            n.set(c)
            e2.set("")
    

    except:
        e2.set("Error: Please enter integers from 0-100!")
        

def zero():
    global x
    global w
    x.set(0.00)
    w.set(100.00)
    e.set("")


#--------------------------------------------------------------------

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

#---------------------------------------------------------------------

calcButton = Button(root, text = "Add to grade", command = add)
calcButton.place(x=350, y=20, height=25, width=150)

subButton = Button(root, text = "Subtract from grade", command = sub)
subButton.place(x=350, y=55, height=25, width=150)

zeroButton = Button(root, text = "Reset", command = zero)
zeroButton.place(x=350, y=90, height=25, width=150)

#---------------------------------------------------------------------

yourGradeLabel = Label(root, text="Your grade:", font=("default", 15))
yourGradeLabel.place(x=20, y=150, height=25, width=200)

yourGradeValLabel = Label(root, textvariable=x, font=("default", 15))
yourGradeValLabel.place(x=220, y=150, height=25, width=100)


weightRemLabel = Label(root, text="Weight remaining:", font=("default", 15))
weightRemLabel.place(x=20, y=180, height=25, width=200)

weightRemValLabel = Label(root, textvariable=w, font=("default", 15))
weightRemValLabel.place(x=220, y=180, height=25, width=100)

#---------------------------------------------------------------------

errorLabel = Label(root, textvariable = e2, font=("default", 10), fg = "red")
errorLabel.place(x=30, y=220, height=20, width=300)

wantEntry = Entry(root)
wantEntry.place(x=135, y=250, height=25, width=100)
gradeLabel = Label(root, text="Grade Wanted (0-100)")
gradeLabel.place(x=110, y=285, height=25, width=150)

wantButton = Button(root, text = "Calculate", command = calc)
wantButton.place(x=350, y=250, height=25, width=150)

yourGradeLabel = Label(root, text="Grade needed:", font=("default", 15))
yourGradeLabel.place(x=20, y=400, height=25, width=200)

yourGradeValLabel = Label(root, textvariable=n, font=("default", 15))
yourGradeValLabel.place(x=220, y=400, height=25, width=100)






root.mainloop() #runs main root window
