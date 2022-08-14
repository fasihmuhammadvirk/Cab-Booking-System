from tkinter import *
from tkinter.messagebox import showerror
import random
import driver as D
import administrator as A
import customer as C 


d = D.driver_login() 
c = C.customer_login()   
a = A.adminlogin()
   

def main():
    
    
    root = Tk()  
    root.geometry('410x350+400+200')  
    def func():
        root.destroy()
        b.view()
        b.goto()
        
    root.title('Cab Booking')
    label_0 = Label(root, text="Login Window",width=25,font=("times new roman",20,"bold"))
    label_0.place(x=90,y=53)
    
    Button(root, text='Login As Customer',width=15,command= c.login).place(x=120,y=160)
    Button(root, text='Login As Admin',width=15,command = a.alogin).place(x=120,y=210)
    Button(root, text='Login As Driver',width=15,command = d.dlogin ).place(x=120,y=260)
    
    root.mainloop()

main()
