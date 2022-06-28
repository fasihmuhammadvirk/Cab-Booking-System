from tkinter import *
from tkinter.messagebox import showerror
import random
from random import randint

    
class driver_login:
       
    def dlogin(self):
        
        
        root = Tk()
        root.geometry('500x400')
        root.title("Loging Page")
        
        global e1 
        global e2
        global e3
        
        label_0 = Label(root, text="Loging",width=20,font=("times new roman",15,"bold"))
        label_0.place(x=150,y=53)
        
        
        label_1 = Label(root, text="Driver Name",font=("times new roman",15,"bold"))
        label_1.place(x=80,y=130)
        
        e1 = Entry(root)
        e1.place(x=240,y=130)
        
    
        label_2 = Label(root, text="Password",width=20,font=("times new roman",15,"bold"))
        label_2.place(x=34,y=180)
        
        e3 = Entry(root,show='*')
        e3.place(x=240,y=180)
        
        Button(root, text='Login Now',width=15,command=self.logged).place(x=180,y=230)
        
        root.mainloop()

 
    def validator(self):
        
        name = e1.get()
        password = e3.get()
        
        with open("driverlogin.txt", "r") as r:
            while True:
                n = r.readline()
                s = r.readline()
                if not n and not s:
                    break
                if n == name + "\n"  and s == password + "\n":
                    return True
                    break
        e1.delete(0,END)
        e3.delete(0,END)
        e1.focus_set()
        
        
    
        r.close()
        
    def view(self):
        
        with open("booked.txt", "r") as f:
            au = open("booking.txt","r")
            while True:
                d = e1.get()
                
                uid = au.readline()
                date = au.readline()
                start = au.readline()
                end = au.readline()
                s = au.readline()
                
                u = f.readline()
                driver = f.readline()
                if not u and not driver :
                    showerror(title = "Error", message = f'No Trip for you Today')
                    break
                
                if u == uid and d + '\n' == driver:
                        showerror(title = "Error", message = f'''              Your Trip is Booked
                                                                 User {uid} , On {date},From {start} , To {end}''')
                        break
                        
                    
    

    
    
    def logged(self):
        if self.validator():
            self.main()
            
        else:
            showerror(title = "Error", message = "Enter Correct Information")
            
    def main(self):
        root = Tk()
        root.geometry('400x150')
        root.title("Loging Page")
        
        label_0 = Label(root, text="View Todays Your Trip",width=20,font=("times new roman",15,"bold"))
        label_0.place(x=100,y=43)
        
        Button(root, text='View Trip',width=15,command= self.view).place(x=110,y=90)
        
        root.mainloop()

        

