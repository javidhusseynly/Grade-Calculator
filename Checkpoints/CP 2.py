from tkinter import *



    
root = Tk()   #making our root window 'root'

x = StringVar()
x.set(0)


gradeEntry = Entry(root)
gradeEntry.place(x=50, y=100, height=25, width=100)
gradeLabel = Label(root, text="Grade (0-100)")
gradeLabel.place(x=50, y=135, height=25, width=100)

weightEntry = Entry(root)
weightEntry.place(x=200, y=100, height=25, width=100)
weightLabel = Label(root, text="Weight (0-100)")
weightLabel.place(x=200, y=135, height=25, width=100)

def calc():
    global x
    try:
        y = int(gradeEntry.get())
        z = int(weightEntry.get())
        a = int(x.get()) + y*z
        x.set(a)
        
    except:
        print("sfas")



calcButton = Button(root, text = "Add to grade", command = calc)
calcButton.place(x=350, y=100, height=25, width=75)

finalLabel = Label(root, textvariable=x, font=("default", 40))
finalLabel.place(x=250, y=250, height=100, width=100)







root.mainloop() #runs main root window
