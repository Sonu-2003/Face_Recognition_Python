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


#Checking if my directory is present or not, if not I will allocate one
def assure_path_exists(path):
    d=os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)

#1:07:67 Tuesday: This implements The real time clock to my system and it will update after 100 milliseconds
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
    existing=os.path.isFile("TrainingImageLabel\password.txt")
    if existing:
        tf=open("TrainingImageLabel\password.txt","r")
        key=tf.read()
    else:
        master.destroy()
        new_pass=tsd.askstring("Old password is not available",'Please enter a new password',show="*")
        if new_pass==None:
            mess._show(title="No Password entered", message ='Password not set!! Please Try again')
        else:
            tf=open("TrainingImageLabel\password.txt","w")
            tf.write(new_pass)
            mess._show(title='New Password Registered', message="Hey!!New Password registered Successfully!!")
            return
        
        