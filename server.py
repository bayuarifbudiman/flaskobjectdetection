from flask import Flask, render_template, url_for,Response
from flask_socketio import SocketIO,emit
from datetime import datetime
import cv2
import os

app = Flask(__name__)
socketio = SocketIO(app)

video = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier('cascade 20.xml')
image_name = []

@app.route('/')
@app.route('/streaming')
def streaming():
    return render_template('streaming.html',title = 'streaming')

def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = video.read()

        #detect cars in the video
        cars3 = car_cascade.detectMultiScale(frame, 1.3,8)
        take_photo = False
        for (x,y,w,h) in cars3:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            CoordXCentroid = int((x+x+w)/2)
            CoordYCentroid = int((y+y+h)/2)
            ObjectCentroid = (CoordXCentroid,CoordYCentroid)
            cv2.circle(frame, ObjectCentroid, 5, (0,255,0), 5) 

        global image_name 
        entries = os.listdir('D:/Latian/python/flask_imageprocessing/static/gallery/')
        if not image_name == entries:
            image_name = entries
            

        '''day = datetime.today()
        current_day=(day.strftime('%d-%m-%Y'))
        now = datetime.now()
        current_time = now.strftime("%H-%M-%S")
        path = 'D:/Latian/python/flask_imageprocessing/static/gallery/'

        if not cv2.imwrite(path + current_day +"_"+ current_time + ".jpg", frame):
            print("Could not write image")'''
        cv2.imwrite('t.jpg', frame)
       
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/image')
def image():
    '''while True:
        image_name = []
        entries = os.listdir('D:/Latian/python/flask_imageprocessing/static/gallery/')
        if not image_name == entries:
            image_name = entries
            return render_template('image.html',title='image',images=image_name)'''
    return render_template('image.html',title='image',images=image_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
