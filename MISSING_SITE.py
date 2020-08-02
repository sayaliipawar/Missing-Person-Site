# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:39:27 2018

@author: Sayali
"""


from tkinter import *
from tkinter import messagebox
import sqlite3
def create():
    root=Tk()
    Label(root,text="ACCOUNT CREATED SUCCESFULLY",fg="green").pack()
    root.mainloop()

def NewFile():
    global e1,e2,e3
    window=Tk()
    window.title("CREATE NEW ACCOUNT")
    window.geometry("900x600+250+50")
    window.config(background="cyan2")
    lb0=Label(window,text="LOG IN",background="yellow2",fg="brown2", font="Impact 20 bold",bd=2,height=1,
    width=20,relief=RIDGE)
    lb0.place(x=300,y=130)
    lb1=Label(window,text="USERNAME",background="cyan2",fg="brown2",font="Bauhaus93 14 bold ",height=2,
    width=17,relief=FLAT)
    lb1.place(x=200,y=200)
    lb2=Label(window,text="PASSWORD",background="cyan2",fg="brown2",font="Bauhaus93 14 bold ",height=2,
    width=17,relief=FLAT)
    lb2.place(x=200,y=260)
    lb3=Label(window,text="PASSWORD(again)",background="cyan2",fg="brown2",font="Bauhaus93 14 bold ",height=2,
    width=17,relief=FLAT)
    lb3.place(x=180,y=310)
    
    e1 = Entry(window, font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e2 = Entry(window,show="*",width=17,relief=SUNKEN)
    e3 = Entry(window,show="*",width=17,relief=SUNKEN)
    e1.place(x=380,y=210)
    e2.place(x=380,y=270)
    e3.place(x=380,y=320)
    Button(window,text="CREATE",command=db2,font="Impact 17 bold"
    ,background="yellow2",bd=2, fg="brown2",height=1,width=12,relief=GROOVE).place(x=350,y=380)
    window.mainloop()
    
def login():
    global t1,t2
    root.destroy
    window=Tk()
    window.title("LOGIN PAGE")
    window.geometry("900x600+250+50")
    window.config(background="yellow2")
    Label(window,text="LOG IN",background="cyan2",fg="brown2", 
    font="Impact 20 bold",bd=2,height=1,width=20,relief=RIDGE).place(x=300,y=110)
    Label(window,text="USERNAME",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=200,y=200)
    Label(window,text="PASSWORD",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=200,y=260)
    t1 = Entry(window, font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    t2 = Entry(window,show="*",width=17,relief=SUNKEN)
    t1.place(x=380,y=210)
    t2.place(x=380,y=270)
    Button(window,text="LOG IN",command=check,font="Impact 17 bold"
    ,background="cyan2",bd=2, fg="brown2",height=1,width=12,relief=GROOVE).place(x=350,y=330)
    window.mainloop()
    
def check():
    count=0
    conn = sqlite3.connect('user.db')
    cursor1=conn.cursor()
    #cursor1.execute("DROP TABLE USER")
    cursor1.execute("SELECT * from USER")
    all_rows = cursor1.fetchall()
    for row in all_rows:
        if(t1.get()==row[0]):
            count=count+1
    if(count==0):       
        messagebox.showerror("ERROR","USER DOES NOT EXIST")
    else:
        fifo()
    
def error():
    messagebox.showerror("ERROR", "user with this username does not exist")
def fifo():
    rt=Tk()
    rt.title("MISSING PERSON SITE")
    rt.geometry("900x600+250+50")
    rt.config(background="yellow2")
    Label(rt,text="MISSING PERSON SITE",background="cyan",fg="brown2", font="Impact 30 bold",bd=4,height=2,
    width=30,relief=RIDGE).place(x=130,y=55)
    Button(rt,text="FIND",command=missing1,font="Impact 17 bold",background="cyan", fg="brown2",height=1,
    width=12,relief=GROOVE).place(x=350,y=330)          
    rt.mainloop()
    
def missing():
    global e4,e5,e6,e7,e8,e9
    master=Tk()
    master.geometry("900x600+250+50")
    master.config(background="yellow2")
    Label(master, text="ENTER THE DETAILS",fg="cyan",background="brown2",
    font="Impact 20 bold",bd=2,height=1,width=20,relief=RIDGE).place(x=300,y=130)
    Label(master, text="NAME",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=50,y=200)
    Label(master, text="AGE",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=50,y=250)
    Label(master, text="COLOR",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=50,y=300)
    Label(master, text="RELIGION",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=50,y=350)
    Label(master, text="GENDER",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=350,y=200)
    Label(master, text="MISSING DATE",background="yellow2",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=350,y=250)
    
    e4 = Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e5 = Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e6= Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e7 =Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e8 =Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e9 =Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    
    e4.place(x=200,y=210)
    e5.place(x=200,y=260)
    e6.place(x=200,y=310)
    e7.place(x=200,y=360)
    e8.place(x=550,y=260)
    e9.place(x=550,y=210)
    
    Button(master, text='RETRY',command=missing,font="Impact 17 bold",
    background="cyan",bd=2, fg="brown2",height=1,width=12,relief=GROOVE).place(x=240,y=410)
    b1=Button(master, text="Submit",command=db,font="Impact 17 bold" ,background="cyan",
    bd=2, fg="brown2",height=1,width=12,relief=GROOVE)
    b1.place(x=440,y=410)
    root.destroy
    master.mainloop( )

def missing1():
    global e9,e10,e11,e12,e13,e14
    master=Tk()
    master.geometry("900x600+250+50")
    master.config(background="cyan")
    
    Label(master, text="ENTER THE DETAILS",fg="brown2",background="yellow2",font="Impact 20 bold",
    bd=2,height=1,width=20,relief=RIDGE).place(x=300,y=130)
    Label(master, text="NAME",background="cyan",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,width=17,relief=FLAT).place(x=50,y=200)
    Label(master, text="AGE",background="cyan",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,width=17,relief=FLAT).place(x=50,y=250)
    Label(master, text="COLOR",background="cyan",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,width=17,relief=FLAT).place(x=50,y=300)
    Label(master, text="GENDER",background="cyan",fg="brown2",
    font="Bauhaus93 14 bold ",height=2,width=17,relief=FLAT).place(x=350,y=200)
    Label(master, text="RELIGION",background="cyan",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,width=17,relief=FLAT).place(x=50,y=350)
    Label(master, text="MISSING DATE",background="cyan",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,width=17,relief=FLAT).place(x=350,y=250)
    
    e9 = Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e10 = Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e11= Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e12 =Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e13 =Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e14 =Entry(master,font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    
    e9.place(x=200,y=210)
    e10.place(x=200,y=260)
    e11.place(x=200,y=310)
    e12.place(x=200,y=360)
    e13.place(x=550,y=260)
    e14.place(x=550,y=210)
    
    
    Button(master, text='RETRY',command=missing1,font="Impact 17 bold"
     ,background="yellow2",bd=2, fg="brown2",height=1,width=12,relief=GROOVE).place(x=240,y=410)

    b1=Button(master, text="FIND",command=db1,font="Impact 17 bold" ,background="yellow2",bd=2, 
    fg="brown2",height=1,width=12,relief=GROOVE)
    b1.place(x=440,y=410)
    root.destroy
    master.mainloop( )

def About():
    window=Tk()
    window.geometry("900x600+250+50")
    window.config(background="cyan2")
    Label(window,text="ABOUT OUR SITE",background="yellow2",fg="brown2", font="Impact 20 bold",bd=2,
    height=1,width=20,relief=RIDGE).place(x=300,y=60)
    Label(window,text="RESPONSIBILITIES",font="Impact 20 bold",background="cyan2").place(x=10,y=110)
    Label(window,text="PREVENTION OF CRIME",font="Impact 20 bold",background="cyan2").place(x=10,y=200)
    Label(window,text="Surveillance on criminals."
          +"\n Monitoring of records."
          +"\nBeat patrolling, mobile and foot patrolling, surprise checks (Naka Bandis),combing operations and raids.",
          font="Impact 12",background="cyan2").place(x=10,y=250)
    Label(window,text="DETECTION OF CRIME",font="Impact 20 bold",background="cyan2").place(x=10,y=320)
    lb3=Label(window,text="Investigation and prosecution of offenders."
          +"\nMAINTENANCE OF PUBLIC ORDER"
          +"\nMaintenance of law and order during festivals, elections,"
          +"\nMaintenance of Internal Security: VIP security and counter espionage.",background="cyan2",font="Impact 12")
    lb3.place(x=10,y=360)        
    window.mainloop()
    
def Contact():
    rt=Tk()
    rt.title("HAPPY TO HELP YOU")
    rt.geometry("900x300")
    rt.config(background="yellow2")
    lb1=Label(rt,text="CONTACT DETAILS",background="cyan2",fg="brown2", font="Impact 20 bold",bd=2,
    height=1,width=20,relief=RIDGE)
    lb1.place(x=300,y=100)
    Label(rt,text="CONTACT US AT: 98645326"
          +"\nEMAIL ID: missingxyz@gmail.com",background="yellow2",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,relief=FLAT).place(x=250,y=200)
    
    rt.mainloop()   
def Adminlogin():  
    global e1,e2;
    root.destroy
    window=Tk()
    window.title("LOGIN PAGE")
    window.geometry("900x600+250+50")
    window.config(background="yellow2")
    lb1=Label(window,text="LOG IN",background="cyan2",fg="brown2", font="Impact 20 bold",bd=2,
    height=1,width=20,relief=RIDGE)
    lb1.place(x=300,y=130)
    lb2=Label(window,text="USERNAME",background="yellow2",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,width=17,relief=FLAT)
    lb2.place(x=200,y=200)
    lb3=Label(window,text="PASSWORD",background="yellow2",fg="brown2",font="Bauhaus93 14 bold ",
    height=2,width=17,relief=FLAT)
    lb3.place(x=200,y=260)
    e1 = Entry(window, font="Bauhaus93 13 bold ",width=17,relief=SUNKEN)
    e2 = Entry(window,show="*",width=25,relief=SUNKEN)
    e1.place(x=380,y=210)
    e2.place(x=380,y=270)      
    Button(window,text="LOG IN",command=check1,font="Impact 17 bold",
    background="cyan2",bd=2, fg="brown2",height=1,width=12,relief=GROOVE).place(x=350,y=330)      
    window.mainloop()

def check1():
    if(str(e1.get())=="sayali"):
        missing()
    else:
        error()
def db():
    conn = sqlite3.connect('missing.db')
    cursor1=conn.cursor()
    #cursor1.execute("DROP TABLE MISSING")
    cursor1.execute('''CREATE TABLE IF NOT EXISTS  MISSING
         (NAME TEXT,
         AGE INT NOT NULL,
         COLOR CHAR(50),
         GENDER TEXT,
         RELIGION TEXT)''')
    cursor1.execute("INSERT INTO MISSING (NAME,AGE,COLOR,GENDER,RELIGION) VALUES ('"+ e4.get()+"','"+e5.get()+"','"+e6.get()+"','"+e7.get()+"','"+e9.get()+"')")
    cursor1.execute("SELECT * from MISSING")
    all_rows = cursor1.fetchall()
    for i in all_rows:
        print(i)
    conn.commit()
    conn.close()
  
def db2():
    conn = sqlite3.connect('user.db')
    cursor1=conn.cursor()
    #cursor1.execute("DROP TABLE USER")
    cursor1.execute('''CREATE TABLE IF NOT EXISTS  USER
         (USERNAME TEXT NOT NULL,
         PASSWORD TEXT NOT NULL)''')
    cursor1.execute("INSERT INTO USER (USERNAME,PASSWORD) VALUES ('"+ e1.get()+"','"+e2.get()+"')")
    cursor1.execute("SELECT * from USER")
    all_rows = cursor1.fetchall()
    for i in all_rows:
        print(i)
    conn.commit()
    conn.close()
    rt=Tk()
    rt.geometry("900x600+250+50")
    rt.config(background="yellow2")
    lb1=Label(rt,text="ACCOUNT CREATED",background="cyan2",fg="brown2", font="Impact 20 bold",bd=2,
    height=2,width=20,relief=RIDGE)
    lb1.place(x=300,y=230)
    
def db1():
   count=0
   conn = sqlite3.connect('missing.db')
   cursor1=conn.cursor() 
   cursor1.execute("SELECT * from MISSING")
   all_rows = cursor1.fetchall()
   for row in all_rows:
       if(row[0]==e9.get()):
           rt=Tk()
           rt.title("MISSING PERSON SITE")
           rt.geometry("900x600+250+50")
           rt.config(background="yellow2")
           lb2=Label(rt,text="PERSON FOUND",background="cyan",fg="brown2", font="Impact 30 bold",bd=4,
           height=2,width=30,relief=RIDGE)
           lb2.place(x=130,y=55)
           count=0
       else:
            count=count+1
   if(count!=0):
        rt=Tk()
        rt.title("MISSING PERSON SITE")
        rt.geometry("900x600+250+50")
        rt.config(background="yellow2")
        lb2=Label(rt,text="PERSON NOT FOUND",background="cyan",fg="brown2", font="Impact 30 bold",
        bd=4,height=2,width=30,relief=RIDGE)
        lb2.place(x=130,y=55)
   conn.commit()
   conn.close()
                                                               
root=Tk()
im2=PhotoImage(file="data.gif")
root.title("MISSING PERSON SITE")
root.geometry("900x600+250+50")
root.config(background="yellow2")
py1=Label(root,image=im2).place(x=220,y=130)
lb2=Label(root,text="MISSING PERSON SITE",background="cyan2",fg="brown1", font="Impact 30 bold",bd=4,
height=2,width=30,relief=RIDGE)
lb2.place(x=130,y=20)
#To crate menubar
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="login", font="Bauhaus93 14 bold ",menu=filemenu)
filemenu.add_command(label="Create New",command=NewFile)
filemenu.add_command(label="log in",command=login)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

helpmenu=Menu(menu)
menu.add_cascade(label="help",menu=helpmenu)
helpmenu.add_command(label="About..",command=About)

adminlogin=Menu(menu)
menu.add_cascade(label="Admin Login",menu=adminlogin)
adminlogin.add_command(label="login",command=Adminlogin)

contactus=Menu(menu)
menu.add_cascade(label="Contact Us",menu=contactus)
contactus.add_command(label="contact",command=Contact)

mainloop()
            