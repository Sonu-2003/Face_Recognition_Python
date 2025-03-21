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

#This is used for taking images and saving my profile.
def clear():
    txt.delete(0,'end')
    res="1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)
    
def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def TakeImages():
    check_haarscas()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails/StudentDetails.csv")
    if exists:
        with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            #This will automatically run the code and allocate serial numbers from 1 to number of candidates
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 6) #KNN- K nearest Neighbours. Just make surr value is within 3 to 7. Apart from this it is not a human face according to science.
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage/ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name]
        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)

def TrainImages():
    check_haarscas()
    assure_path_exists("TrainingImageLabel/")
    recognizer=cv2.face_LBPHFaceRecognizer.create()
    harcascadePath= "haarcascade_frontface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID= getImagesAndLabels("TrainingImage")
    
    try:
        recognizer.train(faces,np.array(ID))
    except:
        mess._show(title="No Registrations", message="Please Register Someone First!!")
        return
    recognizer.save("TrainingImageLabel/")
    res="Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text="Total Registrations till now: "+ str(ID[0]))
    
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    
    #creating  empty lists
    faces=[]
    Ids=[]
    
    #We will loop through the image paths and load the Ids and their corresponding Faces, Eg. 1) Walaa ; 2) Swarnava
    for imagePath in imagePaths:
        #load the face in the computer and convert it to gray scale
        pilImage= Image.open(imagePath).convert('L')
        
        #Now we will convert PIL image into numpy array
        imageNp=np.array(pilImage, 'uint32')
        #uint8- Unique 8 Integers
    

    
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

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ", fg="black",bg="#3ece48" ,font=('times', 17, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res=0
exists = os.path.isfile("StudentDetails/StudentDetails.csv")
if exists:
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')


