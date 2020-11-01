
import random 

from tkinter import *



def generatepassword(): 
	entry.delete(0, END) 

	
	length = var1.get() 

	poor= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	average = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
	strong= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = "" 

	
	if var.get() == 1: 
		for i in range(0, length): 
			password = password + random.choice(poor) 
		return password 

	 
	elif var.get() == 2: 
		for i in range(0, length): 
			password = password + random.choice(average) 
		return password 

	 
	elif var.get() == 3: 
		for i in range(0, length): 
			password = password + random.choice(strong) 
		return password 
	



def generate(): 
	password1= generatepassword() 
	entry.insert(10, password1) 




 
root = Tk() 
var = IntVar() 
var1 = IntVar() 


root.title("Random Password Generator") 
root.geometry("400x100")

label1= Label(root, text="Password") 
label1.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 


label = Label(root, text="Length") 
label.grid(row=1) 



generatebutton = Button(root, text="Generate", command=generate) 
generatebutton.grid(row=1, column=3) 

 
R1= Radiobutton(root, text="Low", variable=var, value=1) 
R1.grid(row=0, column=2 ) 
R2 = Radiobutton(root, text="Medium", variable=var, value=2) 
R2.grid(row=0, column=3 ) 
R3 = Radiobutton(root, text="Strong", variable=var, value=3) 
R3.grid(row=0, column=4)

spinlength=Spinbox(root,from_=8 ,to_=18,textvariable=var1)
spinlength.grid(column=1, row=1)

root.mainloop() 
