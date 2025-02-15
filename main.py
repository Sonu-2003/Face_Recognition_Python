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

#1:07:67 Tuesday: This implements The real time to my system and it will update after 200 milliseconds
def tick():
    time_string= time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(100,tick)

#haarcascadeFile - It is a XML file that vasically ensures that my face recognition model is working with the proper coordinates of each face

