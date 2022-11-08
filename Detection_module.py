import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image


def DetectImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message, text_to_speech):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Id = getImagesandLabels(trainimage_path)
    recognizer.train(faces, np.array(Id))
    recognizer.save(trainimagelabel_path)
    res = "Image Captured Sucessfully" # +",".join(str(f) for f in Id)
    message.configure(text = res)
    text_to_speech(res)
    

def getImagesandLabels(path):
    newdir = [os.path.join(path, d) for d in os.listdir(path)]
    imagepath = [
        os.path.join(newdir[i], f)
        for i in range(len(newdir))
        for f in os.listdir(newdir[i])
    ]
    faces = []
    Ids = []
    for imagepath in imagepath:
        pilImage = image.open(imagepath).convert("L")
        imageNp = np.array(pilImage, "uint8")
        Id = int(os.path.split(imagepath)[-1].split("_")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids