import face_recognition
import cv2
import numpy as np
import pyautogui
from selenium import webdriver
import time
import os

gmail = "divyadarsheedas@gmail.com"
password = "pass"

video_capture = cv2.VideoCapture(0)

root_image = face_recognition.load_image_file("YOUR PHOTO PATH")
root_encoding = face_recognition.face_encodings(root_image)[0]

known_face_encodings = [
    root_encoding,
]
known_face_names = [
    "YOUR NAME",
]

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:,:,::-1]