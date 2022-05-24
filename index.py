
from flask import Response
from flask import Flask
from flask import render_template

import cv2
import matplotlib
matplotlib.use('TkAgg')
import math

import rplidar
import serial

import numpy as np
import matplotlib.pyplot as plt

from manuelLauncher import manuelLauncher
from automaticLauncher import automaticLauncher

# initialize a flask object
app = Flask(__name__)
app.register_blueprint(manuelLauncher, url_prefix="/controller")
app.register_blueprint(automaticLauncher, url_prefix="/controller")



@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

@app.route("/run/automatic")
def automatique():
    return render_template("automaticRobot.html")


@app.route("/run/manuel")
def manuel():
    return render_template("controlleRobot.html")


@app.route("/video_feed_camera")
def video_feed_camera():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generateCamera(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")


@app.route("/video_feed_lidar")
def video_feed_lidar():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(lidarScan(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")


def generateCamera():
	# grab global references to the output frame and lock variables
    
    cap = cv2.VideoCapture()
    # The device number might be 0 or 1 depending on the device and the webcam
    cap.open(0, cv2.CAP_DSHOW)
    while(True):
        ret, frame = cap.read()
        # cv2.imshow('frame', frame)

        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
   
def generateLidar():
    fig = plt.figure()


    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)
    i = 0

    line1, = plt.plot(x1, y1, 'ko-')        # so that we can update data later

    while True:
        # update data
        line1.set_ydata(np.cos(2 * np.pi * (x1+i*3.14/2) ) * np.exp(-x1) )

        # redraw the canvas
        fig.canvas.draw()

        # convert canvas to image
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        # img is rgb, convert to opencv's default bgr
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

        (flag, encodedImage) = cv2.imencode(".jpg", img)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(encodedImage) + b'\r\n')
 
        i += 1
        k = cv2.waitKey(33) & 0xFF
        if k == 27:
            break

 

def displayIHM():
        plt.ion()

        fig = plt.figure()
        ax1 = fig.add_subplot(211)

        ax2 = fig.add_subplot(212)

        while True:
            for i, scan in enumerate(serial.iter_scans()):
            #print('%d: Got %d measurments' % (i, len(scan)))

                if(len(scan)>200):
                    data = cleanData(scan,13)
                    X,Y,Theta,R = polarToCartesian(data)

                    ax1.clear()
                    ax2.clear()

                    reax(ax1)

                    ax1.scatter(X, Y, 'b-')
                    ax2.scatter(Theta, R, 'r-')
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    #time.sleep(0.4)

            img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                    sep='')
            img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

            # img is rgb, convert to opencv's default bgr
            img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

            (flag, encodedImage) = cv2.imencode(".jpg", img)
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
                bytearray(encodedImage) + b'\r\n')
    
            i += 1
            k = cv2.waitKey(33) & 0xFF
            if k == 27:
                break

def polarToCartesian(data):
    data = cleanData(data)
    X = []
    Y = []
    Theta= []
    R = []

    for coord in data:
        X.append(coord[1]*math.cos(np.radians(coord[0])))
        Y.append( coord[1]*math.sin(np.radians(coord[0])))
        Theta.append(coord[0])
        R.append(coord[1])

    return X,Y,Theta,R		


def reax(ax):
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

def cleanData(data):
    clean_data = []

    for coord in data:
        clean_data.append(f"{coord[0]},{coord[1]},{coord[2]}")

    return clean_data


def get_data():
    lidar = rplidar.RPLidar('ttyUSB0', baudrate=115200)
    for scan in lidar.iter_scans(max_buf_meas=500):
        break
    lidar.stop()
    return scan

def lidarScan():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    i = 0
    
    while True:
        if(i%7==0):
            x = []
            y = []
        current_data=get_data()
        for point in current_data:
            if point[0]==15:
                x.append(point[2]*np.sin(np.radians(point[1])))
                y.append(point[2]*np.cos(np.radians(point[1])))

        ax.scatter(x, y, s=0.5, c="limegreen")
        ax.axis('equal')
        ax.axis('off')
        fig.canvas.draw()
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        # img is rgb, convert to opencv's default bgr
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

        (flag, encodedImage) = cv2.imencode(".jpg", img)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(encodedImage) + b'\r\n')

        i += 1
        k = cv2.waitKey(33) & 0xFF
        if k == 27:
            break
# check to see if this is the main thread of execution
if __name__ == '__main__':
	# start the flask app
	app.run( debug=True,
		threaded=True, use_reloader=False)
# release the video stream pointer




