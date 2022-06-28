from tkinter import *
from tkinter.messagebox import showerror
import random
from random import randint

#for requesting for booking 
class Booking:
    
    def main(self):
        
        root = Tk()
        root.geometry('500x500')
        root.title("Booking")

        label_0 = Label(root, text="Booking Request",width=20,font=("bold", 20))
        label_0.place(x=110,y=53)
        
        
        global entry1
        global d
        global m
        global y
        global de
        global aa
        global var1
        global var2
        
        def func():
            pass
        

        label_1 = Label(root, text="User ID",width=20,font=("times new roman",15,"bold"))
        label_1.place(x=60,y=130)

        entry1 = Entry(root)
        entry1.place(x=240,y=130)

        label_2 = Label(root, text="Select Date",width=20,font=("times new roman",15,"bold"))
        label_2.place(x=68,y=180) 
        listx = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
        d = StringVar()
        droplists = OptionMenu(root,d, *listx)
        droplists.config(width=3)
        d.set('DATE')
        droplists.place(x=240,y=180)
        
        
        listy = ['1','2','3','4','5','6','7','8','9','10','11','12'];
        m=StringVar()
        droplist=OptionMenu(root,m, *listy)
        droplist.config(width=5)
        m.set('MONTH') 
        droplist.place(x=310,y=180)

        listz = ['2019','2020','2021','2022','2023','2024','2025'];
        y=StringVar()
        droplist=OptionMenu(root,y, *listz)
        droplist.config(width=3)
        y.set('YEAR') 
        droplist.place(x=400,y=180)



        label_3 =  Label(root, text=" From To ",width=20,font=("times new roman",15,"bold"))
        label_3.place(x=65,y=230)
        list1 = ['Home adress','Gulberg','DHA phase1','DHA phase2','DHA phase3','DHA phase4','DHA phase5','DHA phase6','DHA phase8','Model Town','Faisal Town','Johar Town','Cantt'];
        de=StringVar()
        droplist=OptionMenu(root,de, *list1)
        droplist.config(width=15)
        de.set('Departure') 
        droplist.place(x=235,y=230)



        label_4 = Label(root, text="To Place",width=20,font=("times new roman",15,"bold"))
        label_4.place(x=65,y=280)
        list2 = ['Home adress','Gulberg','DHA phase1','DHA phase2','DHA phase3','DHA phase4','DHA phase5','DHA phase6','DHA phase8','Model Town','Faisal Town','Johar Town','Cantt'];
        aa =StringVar()
        droplist=OptionMenu(root,aa, *list2)
        droplist.config(width=15)
        aa.set('Arrival') 
        droplist.place(x=235,y=280) 

        label_4 = Label(root, text="Option",width=20,font=("times new roman",15,"bold"))
        label_4.place(x=65,y=330)
        var1 = IntVar()
        Checkbutton(root, text="Single", variable=var1).place(x=235,y=330)
        var2 = IntVar()
        Checkbutton(root, text="Multiple", variable=var2).place(x=290,y=330)
        

        Button(root, text='Book Now',width=15,command = self.book ).place(x=180,y=380)

        root.mainloop()
        
        
    def book(self):
        
        showerror(title = "Information", message = 'Your Request has been submitted')
        
        e1 = entry1.get()
        e2 = d.get()
        e3 = m.get()
        e4 = y.get()
        e5 = de.get()
        e6 = aa.get()
        e7 = var1.get()
        e8 =var2.get()
        

        with open("booking.txt","a") as a:
            
            a.write(str(e1)+'\n')
            a.write(str(e2)+'-')
            a.write(str(e3)+'-')
            a.write(str(e4)+'\n')
            a.write(str(e5)+'\n')
            a.write(str(e6)+'\n')
            if e8 == 1:
                a.write('Multiple'+'\n')
            else:
                a.write('Single'+'\n')
            
        a.close()
        

#for registring new user/customer 
class registration():
    
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
        e3 = random.randint(0,5000)
        Button(tkWindow, text='Register',width=15,command = self.register).place(x=140,y=210)
        
        
        tkWindow.mainloop()
        
        

    def register(self):
        
        
        showerror(title = "Error", message = f'Your User ID is {e3}\n Dont Forget')
        
        
        username = e1.get()
        password = e2.get()
        userid = e3

        with open("Userlogin.txt","a") as au:
        
            au.write( str(username) + "\n")
            au.write(str(password) + "\n")
            au.write( str(userid) + "\n")
            
            e1.delete(0,END)
            e2.delete(0,END)
            e1.focus_set()
            
            
        au.close()
    
    
        

#main customer class 
class customer:
     
    def main(self):
        c = customer_login()
        b = Booking()
        root = Tk()  
        root.geometry('410x350+400+200')  
        root.title('Cab Booking')
        label_0 = Label(root, text="Welcome Into Cab Booking",width=25,font=("times new roman",20,"bold"))
        label_0.place(x=90,y=53)
        
        Button(root, text='Request For Booking',width=15,command= b.main).place(x=120,y=160)
        Button(root, text='View Booking Detail',width=15,command = c.view).place(x=120,y=210)
            
        root.mainloop()

                
       
#customer login validation class 
    
class customer_login:
    
    
    def login(self):
        
        r =registration()
        
        
        root = Tk()
        root.geometry('500x500')
        root.title("Loging Page")
        
        global e1 
        global e2
        global e3
        
        label_0 = Label(root, text="Loging",width=20,font=("times new roman",15,"bold"))
        label_0.place(x=150,y=53)
        
        
        label_1 = Label(root, text="User Name",font=("times new roman",15,"bold"))
        label_1.place(x=80,y=130)
        
        e1 = Entry(root)
        e1.place(x=240,y=130)
        
        label_1 = Label(root, text="User ID",font=("times new roman",15,"bold"))
        label_1.place(x=80,y=180)
        
        e2 = Entry(root)
        e2.place(x=240,y=180)

        label_2 = Label(root, text="Password",width=20,font=("times new roman",15,"bold"))
        label_2.place(x=34,y=230)
        
        e3 = Entry(root,show='*')
        e3.place(x=240,y=230)
        
        Button(root, text='Login Now',width=15,command=self.logged).place(x=180,y=280)
        Button(root, text='Regiter',width=15,command = r.main).place(x=180,y=330)
        
        root.mainloop()

 
    def validator(self):
        
        name = e1.get()
        userid = e2.get()
        password = e3.get()
        
        with open("Userlogin.txt", "r") as r:
            while True:
                n = r.readline()
                s = r.readline()
                i = r.readline()
                if not n and not s and not i :
                    break
                if n == name + "\n"  and s == password + "\n" and i == userid + "\n" :
                    return True
                    break
        e1.delete(0,END)
        e2.delete(0,END)
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
                    
                    
    

    def cancle(self):
        
        
        with open("booked.txt", "r") as f:
            
            bookings = f.readlines()
            
        with open("booked.txt", "w") as f:
            
            z = 0
            s =1
            
            
            for i in bookings:
                userid = e2
                
                u = bookings[bookings.index(i)+z]
                d = bookings[bookings.index(i)+s]
                
                
                z = z+1
                s = s+1
                
                
                print(u)
                if not u and not d:
                    showerror(title = "Error", message = f'Your Request is Still Pending')
                    break
                
                if u == str(userid) + '\n':
                        showerror(title = "Error", message = f'Your Cab Booking is Cancled')
                        break
                else:
                    f.write(u)
                    f.write(d)
                    

        
        
        
        
        
       
      
    
    def logged(self):
        if self.validator():
            c = customer()
            c.main()
        else:
            showerror(title = "Error", message = "Enter Correct Information")
    

c = customer_login()
c.login()
    

     