#import libraries of python opencv
import cv2
import numpy as np

import time
prevTime = 0

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return hours, mins, sec

#create VideoCapture object and read from video file
cap = cv2.VideoCapture(0)
#fgbg = cv2.createBackgroundSubtractorMOG2()
#use trained cars XML classifiers
car_cascade = cv2.CascadeClassifier('cascade 20.xml')
#daftar = 200
#daftar2 = 1000
#read until video is completed
while True:
    #capture frame by frame
    ret, frame = cap.read()

    #define region of interest
    '''roi = frame[400:900 , 500:1000]    
    cv2.rectangle(frame,(500,400),(1000,900),(0,255,0),5)
    '''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #roi = frame[250:550 , 350:700]
        
    #cv2.rectangle(frame,(350,250),(700,550),(0,255,0),5)

    #roi = frame[100:550 , 350:550]
        
    #cv2.rectangle(frame,(350,100),(550,550),(0,255,0),5)
    #hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
    #convert video into gray scale of each frames
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #cars2 = fgbg.apply(gray)
    
    #detect cars in the video
    cars3 = car_cascade.detectMultiScale(frame, 1.3,7)

    #to draw arectangle in each cars 
    for (x,y,w,h) in cars3:
        #cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        CoordXCentroid = int((x+x+w)/2)
        CoordYCentroid = int((y+y+h)/2)
        ObjectCentroid = (CoordXCentroid,CoordYCentroid)
        #cv2.circle(roi, ObjectCentroid, 5, (0,255,0), 5)
        cv2.circle(frame, ObjectCentroid, 5, (0,255,0), 5)
        #start_time = time.time()
        #end_time = time.time()
        #time_lapsed = end_time - start_time
        #jam, menit, detik = time_convert(time_lapsed)
        #a=("Time Lapsed = {0}:{1}:{2}".format(int(jam),int(menit),int(detik)))
        #cv2.putText(frame, a, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),3)
        #display the resulting frame
    cv2.imshow('video', frame)
    #cv2.imshow('nganu',gray)
    #cv2.imshow('grayscale',cars2)
    
    #press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#release the videocapture object
cap.release()
#close all the frames
cv2.destroyAllWindows()
