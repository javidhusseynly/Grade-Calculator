import tkinter as tk

x = 0

    
root = tk.Tk()   #making our root window 'root'



gradeEntry = tk.Entry(root)
gradeEntry.place(x=50, y=100, height=25, width=100)
gradeLabel = tk.Label(root, text="Grade (0-100)")
gradeLabel.place(x=50, y=135, height=25, width=100)

weightEntry = tk.Entry(root)
weightEntry.place(x=200, y=100, height=25, width=100)
weightLabel = tk.Label(root, text="Weight (0-100)")
weightLabel.place(x=200, y=135, height=25, width=100)

def calc():
    global x
    try:
        y = int(gradeEntry.get())
        z = int(weightEntry.get())
        x = x + y*z
        finalLabel = tk.Label(root, text=x, font=("default", 40))
        finalLabel.place(x=250, y=300, height=100, width=100)
        
    except:
        print("sfas")



calcButton = tk.Button(root, text = "Add to grade", command = calc)
calcButton.place(x=350, y=100, height=25, width=75)

##delButton = tk.Button(root, text = "Del inshallah", command = del)
##delButton.place(x=350, y=200, height=25, width=75)

finalLabel = tk.Label(root, text=x, font=("default", 40))
finalLabel.place(x=250, y=250, height=100, width=100)







root.mainloop() #runs main root window
