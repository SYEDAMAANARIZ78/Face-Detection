import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk,  Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# Project Module

import Detection_module

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()
    
    
haarcasecade_path = "D:\GitHub Repository\Face-Detection\haarcascade_frontalface_default.xml"
trainimagelabel_path = ("D:\GitHub Repository\Face-Detection\ImageLabel")
trainimage_path = "D:\GitHub Repository\Face-Detection\Detected_Image"
    
    
window = Tk()
window.title("Face Detector")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure you want to close?"
window.configure(background= "black")

# to destroy screen
def del_sc1():
    sc1.destroy()
    
    
def trainimageUI():
    ImageUI = Tk()
    ImageUI.title("Take Image...")
    ImageUI.geometry("780x480")
    ImageUI.configure(background= "black")
    ImageUI.resizable(0, 0)
    
    
    def train_image():
        Detection_module.DetectImage(
            haarcasecade_path, 
            trainimage_path, 
            trainimagelabel_path, 
            message, 
            text_to_speech
        )
    
    trainImg = tk.Button(
        ImageUI,
        text = "Take Image",
        command = train_image,
        bd = 10,
        font = ("Arial", 18),
        bg  = "black",
        fg = "green",
        height = 2,
        width = 12,
        relief = RIDGE,
    )
    trainImg.place(x = 240, y = 250)

r = tk.Button(
    window,
    text="Recognize A Face",
    command=trainimageUI,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=540, y=280)
    
window.mainloop()

 