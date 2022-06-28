from tkinter import *
from tkinter.messagebox import showerror
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sys


class adminlogin:
    
    def alogin(self):
        
        r = registration()
        
        root = Tk()
        root.geometry('500x500')
        root.title("Loging Page")
        
        global e1 
        global e2
        global e3
        
        label_0 = Label(root, text="Loging",width=20,font=("times new roman",15,"bold"))
        label_0.place(x=150,y=53)
        
        
        label_1 = Label(root, text="Admin User Name",font=("times new roman",15,"bold"))
        label_1.place(x=80,y=130)
        
        e1 = Entry(root)
        e1.place(x=240,y=130)
        
        
        label_2 = Label(root, text="Password",width=20,font=("times new roman",15,"bold"))
        label_2.place(x=34,y=230)
        
        e3 = Entry(root,show='*')
        e3.place(x=240,y=230)
        
        Button(root, text='Login Now',width=15,command=self.logged).place(x=180,y=280)
        Button(root, text='Create New Admin',width=15,command = r.main).place(x=180,y=330)
        
        root.mainloop()

 
    def validator(self):
        
        name = e1.get()
        password = e3.get()
        
        with open("adminlogin.txt", "r") as r:
            while True:
                n = r.readline()
                s = r.readline()
                if not n and not s :
                    break
                if n == name + "\n"  and s == password + "\n" :
                    return True
                    break
        e1.delete(0,END)
        e3.delete(0,END)
        e1.focus_set()
        
        
    
        r.close()
        
    def view(self):
        
        with open("booked.txt", "r") as f:
            
            while True:
                userid = e2.get()
                u = f.readline()
                driver = f.readline()
                if not u and not driver :
                    showerror(title = "Error", message = f'Your Request is Still Pending')
                    break
                
                if u == str(userid) + '\n':
                        showerror(title = "Error", message = f'Your Cab is Booked, Your Dirver is {driver}')
                        break
    
    def logged(self):
        if self.validator():
            a = adminstration()
            a.main()
        else:
            showerror(title = "Error", message = "Enter Correct Information")
    
class registration:
    
    def main(self):
        
       	tkWindow = Tk()  
       	tkWindow.geometry('410x350+400+200')  
       	tkWindow.title('Login Form')
       	windows = tkWindow
       
       	def ext():
       		windows.destroy()
       
       	title =   Label(tkWindow,text = "Register HERE",font=("times new roman",20,"bold"),fg = "red").place(x = 150 , y = 30)
       			
       	global e1
       	global e2
        global e3
        
        
       
       	#username label and text entry box
       	usernameLabel = Label(tkWindow,text = "Username",font=("times new roman",15,"bold")).place(x = 50 , y = 100)
       	e1 = Entry(tkWindow)
       	e1.place(x=150,y=100,width =200)
       
       
       	#password label and password entry box
       	passwordLabel = Label(tkWindow,text = "Password",font=("times new roman",15,"bold")).place(x = 50 , y = 150)
       	e2 =  Entry(tkWindow, show='*')
       	e2.place(x=150,y=150,width =200)        
        Button(tkWindow, text='Register',width=15,command = self.register).place(x=140,y=210)
        
        
        tkWindow.mainloop()
        
        

    def register(self):
        
        
        showerror(title = "Error", message = f'Admin Created')
        
        
        username = e1.get()
        password = e2.get()
        
        with open("adminlogin.txt","a") as au:
        
            au.write( str(username) + "\n")
            au.write(str(password) + "\n")
            
            e1.delete(0,END)
            e2.delete(0,END)
            e1.focus_set()
            
            
        au.close()
        
        
        
class registration_c:
    
    def main(self):
        
       	tkWindow = Tk()  
       	tkWindow.geometry('410x350+400+200')  
       	tkWindow.title('Login Form')
       	windows = tkWindow
       
       	def ext():
       		windows.destroy()
       
       	title =   Label(tkWindow,text = "Add Driver",font=("times new roman",20,"bold"),fg = "red").place(x = 150 , y = 30)
       			
       	global e1
       	global e2
        global e3
        
        
       
       	#username label and text entry box
       	usernameLabel = Label(tkWindow,text = "His Username",font=("times new roman",15,"bold")).place(x = 50 , y = 100)
       	e1 = Entry(tkWindow)
       	e1.place(x=150,y=100,width =200)
       
       
       	#password label and password entry box
       	passwordLabel = Label(tkWindow,text = "His Password",font=("times new roman",15,"bold")).place(x = 50 , y = 150)
       	e2 =  Entry(tkWindow, show='*')
       	e2.place(x=150,y=150,width =200)        
        Button(tkWindow, text='Register',width=15,command = self.register).place(x=140,y=210)
        
        
        tkWindow.mainloop()
        
        

    def register(self):
        
        
        showerror(title = "Error", message = f'Driver Added')
        
        
        username = e1.get()
        password = e2.get()
        
        with open("driverlogin.txt","a") as au:
        
            au.write( str(username) + "\n")
            au.write(str(password) + "\n")
            
            e1.delete(0,END)
            e2.delete(0,END)
            e1.focus_set()
            
            
        au.close()


class booking_detail:
    def view(self):
        

        root = tk.Tk()
        root.geometry('400x400')
        root.resizable(False, False)
        root.title('Booking Request')

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # create a list box
        bo = open('booking.txt','r')
        langs = bo.readlines()
        langs_var = tk.StringVar(value=langs)

        listbox = tk.Listbox(
            root,
            listvariable=langs_var,
            height=10,
            selectmode='extended')

        listbox.grid(
            column=0,
            row=0,
            sticky='nwes'
        )

        # handle event
        def items_selected(event):
            """ handle item selected event
            """
            # get selected indices
            selected_indices = listbox.curselection()
            # get selected items
            selected_langs = ",".join([listbox.get(i) for i in selected_indices])
            msg = f'You selected: {selected_langs}'

            showinfo(
                title='Information',
                message=msg)


        listbox.bind('<<ListboxSelect>>', items_selected)

        root.mainloop()
        
    def goto(self):
        a = adminstration()
        a.main()
        
class assign_booking:
    
    def assign(self):
        d = open('driverlist.txt','r')
        au = open('booking.txt','r')
        bb = open('booked.txt','r')

            
        booked = bb.readlines()
        while True:
            
            uid = au.readline()
            date = au.readline()
            start = au.readline()
            end = au.readline()
            s = au.readline()
            driver = d.readline()
            
            if not driver :
                showinfo(
                    title='Information',
                    message='No Driver Avaible')
                sys.exit()
            elif not uid :
                showinfo(
                    title='Information',
                    message='No Customer Avaible')

                sys.exit()
            
            
            for i in booked:
                if i == driver:
                    if uid == booked:
                        showinfo(
                        title='Information',
                        message= 'Already Booked')
                        
 
            for i in booked:
                if driver in booked:
                    
                    showinfo(
                        title='Information',
                        message='No Driver Avaliable Today')
                    sys.exit()
                else:
                    
                    bc = open('booked.txt','a')
                    bc.write(uid)
                    bc.write(driver)
                    showinfo(
                        title='Information',
                        message='Customer has Assign a Dirver')
                    break
        

            else:
                break
            


        
        
class adminstration:
    
    def main(self):
        
        
        root = Tk()  
        root.geometry('410x350+400+200')  
        c = registration_c()
        b = booking_detail()
        a = assign_booking()
        def func():
            root.destroy()
            b.view()
            b.goto()
            
        root.title('Cab Booking')
        label_0 = Label(root, text="Admin Window",width=25,font=("times new roman",20,"bold"))
        label_0.place(x=90,y=53)
        
        Button(root, text='Add Driver',width=15,command= c.main).place(x=120,y=160)
        Button(root, text='View Booking Detail',width=15,command = func).place(x=120,y=210)
        Button(root, text='Assign Booking',width=15,command = a.assign ).place(x=120,y=260)
        
        root.mainloop()

    

    
    
    
    
    
    
    
    
    


        
    