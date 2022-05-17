# from pyimagesearch.motion_detection import SingleMotionDetector

from flask import Response
from flask import Flask
from flask import render_template
import cv2

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


@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")


def generate():
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
   

		



# check to see if this is the main thread of execution
if __name__ == '__main__':
	# start the flask app
	app.run( debug=True,
		threaded=True, use_reloader=False)
# release the video stream pointer




