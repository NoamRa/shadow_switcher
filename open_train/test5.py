import cv2, platform
import numpy as np
import urllib
import os



def display_versions():
    # displays the version number of Python, Numpy and OpenCV.
    print "Python's version is " + platform.python_version()
    print "Numpy's  version is " + np.__version__
    print "OpenCV's version is " + cv2.__version__

display_versions()

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)
winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)


print "Press 'q' to quit."
# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:
    cv2.imshow( winName, diffImg(t_minus, t, t_plus) )
    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    # Press q to quit.    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# cam2.release()
cv2.destroyAllWindows()