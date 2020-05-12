from tkinter import *

    
root = Tk()   #making our root window 'root'
root.geometry("1000x700")
x = StringVar()
x.set(0.00)

w = StringVar()
w.set(100.00)

e = StringVar()
e.set("")

e2 = StringVar()
e2.set("")

n = StringVar()
n.set(0.00)

yval = 120
recentMark = 0

#adds to mark
def add():
    global recentMark
    try:
        a = float(gradeEntry.get())
        b = float(weightEntry.get()) / 100
        if ( (b*100) > float(w.get())):
            e.set("Error: That is over 100 total weight!")
        elif (a<=100) and (b<=1):
            c = round((float(x.get()) + a*b ), 2)
            if c < 0:
                e.set("Error: That is under 100 total grade!")
            else:
                x.set(c)
                d = round((float(w.get()) - (b*100)), 2)
                w.set(d)
                recentMark = c
                e.set("")
        else:
            e.set("Error: Please enter integers from 0-100!z")
        
    except:
        e.set("Error: Please enter integers from 0-100!")
    

#subtracts mark from grade
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


#calculates grade required
def calc():
    try:
        a = float(wantEntry.get())
        if (a > 100) or (a < 0):
            e2.set("Error: Please enter an dsasdinteger from 0-100!")
        else:
            b = (a - (float(x.get())))
            c = round( ((b/ (float(w.get())))*100), 2)
            n.set(c)
            e2.set("")
        

    except:
        e2.set("Error: Please enter integers from 0-100!")

def addToList():
    global yval
    print("add to list function = running")
    className = nameClassEntry.get()
    classGrade = recentMark
    Label(root, text = className, font = ("default", 15)).place(x=650, y = yval, height = 25, width = 200)
    Label(root, text = classGrade, font = ("default", 15)).place(x=850, y = yval, height = 25, width = 100)
    yval += 30

def zero():
    x.set(0.00)
    w.set(100.00)
    e.set("")

def zeroW():
    n.set(0.00)


#--------------------------------------------------------------------

#error notification for grade entry
errorLabel = Label(root, textvariable = e, font=("default", 10), fg = "red")
errorLabel.place(x=25, y=15, height=20, width=300)

#entry for grade
gradeEntry = Entry(root)
gradeEntry.place(x=60, y=50, height=25, width=100)
gradeLabel = Label(root, text="Grade (0-100)")
gradeLabel.place(x=60, y=85, height=25, width=100)

#entry for weight
weightEntry = Entry(root)
weightEntry.place(x=190, y=50, height=25, width=100)
weightLabel = Label(root, text="Weight (0-100)")
weightLabel.place(x=190, y=85, height=25, width=100)

#---------------------------------------------------------------------

#button to add to grade
calcButton = Button(root, text = "Add to grade", command = add)
calcButton.place(x=350, y=20, height=25, width=150)

#button to subtract
subButton = Button(root, text = "Subtract from grade", command = sub)
subButton.place(x=350, y=55, height=25, width=150)

#button to zero
zeroButton = Button(root, text = "Reset", command = zero)
zeroButton.place(x=350, y=90, height=25, width=150) 

#---------------------------------------------------------------------

#your grade
yourGradeLabel = Label(root, text="Your grade:", font=("default", 15))
yourGradeLabel.place(x=20, y=150, height=25, width=200)
yourGradeValLabel = Label(root, textvariable=x, font=("default", 15))
yourGradeValLabel.place(x=220, y=150, height=25, width=100)

#weight remaining 
weightRemLabel = Label(root, text="Weight remaining:", font=("default", 15))
weightRemLabel.place(x=20, y=180, height=25, width=200)
weightRemValLabel = Label(root, textvariable=w, font=("default", 15))
weightRemValLabel.place(x=220, y=180, height=25, width=100)

#button to add to class list
nameClassEntry = Entry(root)
nameClassEntry.place(x=350, y=130, height = 25, width = 150)

addToClassButton = Button(root, text = "Add to List", command = addToList)
addToClassButton.place(x=350, y=160, height=25, width=150)

#---------------------------------------------------------------------

#error notification for grade wanted entry
errorLabel = Label(root, textvariable = e2, font=("default", 10), fg = "red")
errorLabel.place(x=30, y=230, height=20, width=300)

#entry for grade wanted
wantEntry = Entry(root)
wantEntry.place(x=135, y=260, height=25, width=100)
gradeLabel = Label(root, text="Grade Wanted (0-100)")
gradeLabel.place(x=110, y=295, height=25, width=150)

#button to calculate grade needed
wantButton = Button(root, text = "Calculate", command = calc)
wantButton.place(x=350, y=245, height=25, width=150)

#zero button
zeroWantButton = Button(root, text = "Reset", command = zeroW)
zeroWantButton.place(x=350, y=280, height=25, width=150)

#your grade
yourGradeLabel = Label(root, text="Grade needed:", font=("default", 15))
yourGradeLabel.place(x=20, y=330, height=25, width=200)
yourGradeValLabel = Label(root, textvariable=n, font=("default", 15))
yourGradeValLabel.place(x=220, y=330, height=25, width=100)


#----------------------------------------------------------------------

#your classes
classesLabel = Label(root, text="Classes", font=("default", 25))
classesLabel.place(x=650, y=70, height=25, width=250)




root.mainloop() #runs main root window
