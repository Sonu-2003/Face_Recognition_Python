import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
import pandas as pd
from PIL import Image
import datetime
import time
#mpl_finance , candle_stick_ohlc

#Checking if my directory is present or not, if not I will allocate one
def assure_path_exists(path):
    d=os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)

#1:07:67 Tuesday: This implements The real time clock to my system and it will update after 100 milliseconds
#Reinforcement Learning- RL
def tick():
    time_string= time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(100,tick)

#Users can contact us through thid message box

def contact():
    mess._show(title="Contact me", message="You can contact us at: swarnava2003.sonu@gmail.com")

#haarcascadeFile - It is a XML file that vasically ensures that my face recognition model is working with the proper coordinates of each face

def check_haarscas():
    exists=os.path.isFile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title="Hey,My Haarscascade File is not available", message="Please contact us for any issues ")
        window.destroy() 


#I will be showing you how to scan and test whether my image is registered in the database. If it's not, it will prompt the admin for changing password
def save_pass():
    assure_path_exists("TrainingImageLabel/")
    existing=os.path.isfile("TrainingImageLabel/password.txt")
    if existing:
        tf=open("TrainingImageLabel/password.txt","r")
        key=tf.read()
    else:
        m.destroy()
        new_pass=tsd.askstring("Old password is not available",'Please enter a new password',show="*")
        if new_pass==None:
            mess._show(title="No Password entered", message ='Password not set!! Please Try again')
        else:
            tf=open("TrainingImageLabel/password.txt","w")
            tf.write(new_pass)
            mess._show(title='New Password Registered', message="Hey!!New Password registered Successfully!!")
            return
    op=(old.get())
    newp=(new.get())
    nnewp=(nnew.get())
    if(op==key):
        if(newp==nnewp):
            txf=open("TrainingImageLabel/password.txt","w")
            txf.write(newp)
        else:
            mess._show(title="Error", message="Hey! Confirm me the new password")
            return
    else:
        mess._show(title="Wrong Password", message="Please enter your correct password")
        return
    mess._show(title="Password changed", message="Hey! Password changed successfully")
    m.destroy()
    
    #In the above code, we are actually Trying to set up a new password and check if the new password is matching with the new password comfirmation.abs
def change_pass():
    global m
    m=tk.Tk()
    m.geometry("300x160")
    m.resizeable(False,False)
    m.title("Change Password")
    m.configure(background="white")
    lbl=tk.Label(m,text=' Enter Old Password  ', bg='white', font=('times',12,'bold'))
    lbl.pack()
    global old
    old=tk.Entry(m,width="25", fg="black", relief="solid", font=('times',12,'bold'),show="*")
    old.pack()
    lbl5=tk.Label(m,text=' Enter Your Password  ', bg='white', font=('times',12,'bold'))
    lbl5.pack()
    global new
    new=tk.Entry(m,width="25", fg="black", relief="solid", font=('times',12,'bold'),show="*")
    new.pack()
    lbl6=tk.Label(m,text=' Enter your new Password  ', bg='white', font=('times',12,'bold'))
    lbl6.pack()
    global nnew
    nnew=tk.Entry(m,width="25", fg="black", relief="solid", font=('times',12,'bold'),show="*")
    nnew.pack()
    lbl7=tk.Label(m,text=' Confirm your new Password  ', bg='white', font=('times',12,'bold'))
    lbl7.pack()
    nnew = tk.Entry(m, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(m,text="Cancel", command=m.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(m, text="Save", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    
    m.mainloop()
    
#Let's create date and time
global key
key=''
ts=time.time()
date=datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }
#GUI-FRONTEND

window=tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background="#262523")
      
frame1=tk.Frame(window,bg="#00aeff")
frame1.place(relx=0.11,rely=0.17,relwidth=0.39,relheight=0.80)

frame2=tk.Frame(window,bg="#00aeff")
frame2.place(relx=0.51,rely=0.17,relwidth=0.39,relheight=0.80)

message3=tk.Label(window,text="Face Recognition Based Attendance System", fg="white",bg="#262523" , width=55,height=1,font=('times',29,'bold'))
message3.pack()

frame3=tk.Frame(window,bg="#c4c6ce")
frame3.place(relx=0.52,rely=0.09,relwidth=0.09,relheight=0.07)

frame4=tk.Frame(window,bg="#c4c6ce")
frame4.place(relx=0.37,rely=0.09,relwidth=0.16,relheight=0.07)



datef=tk.Label(frame4,text= day+"-"+mont[month]+"-"+year+"  |  ",fg="orange",bg="#262523", width=55, height=1,font=('times',22,'bold'))
datef.pack(fill='both',expand=1)

clock=tk.Label(frame3,fg="orange",bg="#262523",width=55,height=1,font=('times',22,'bold'))
clock.pack(fill='both',expand=1)
tick()

head2=tk.Label(frame2,text="  For New Registrations  ",fg="black",bg="#3ece48", font=('times',17,'bold'))
head2.grid(row=0,column=0)

head1=tk.Label(frame1,text="  For Already Registered   ",fg="black",bg="#3ece48", font=('times',17,'bold'))
head1.place(x=0,y=0)
