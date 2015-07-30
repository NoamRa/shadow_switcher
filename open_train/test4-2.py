# testing with SIFT

import cv2, platform
import numpy as np
import urllib
import os


# . ~/.profile
# First
# ffserver -d -f /etc/ffserver.conf
# Second
# ffmpeg -i  mmst://194.90.203.111/cam2 -q 1 http://localhost:8090/cam2.ffm


    # mms://194.90.203.111/cam2
    # ffmpeg -i mmst://194.90.203.111/cam2 -f rtsp rtsp://127.0.0.1:
    # ffplay -i mmst://194.90.203.111/cam2
    # E:\Downloads\ffmpeg-20140830-git-596636a-win64-static\bin
    # ffmpeg -i mmst://194.90.203.111/cam2 -ar 44100 -vcodec libx264  -r 25 -b:v 500k -f flv rtmp://127.0.0.1:1935
    # ffmpeg -i mmst://194.90.203.111/cam2 -f flv "rtp://127.0.0.1:1935/cam2"

    
    # vlc http://192.168.0.103:8080/cam2


def display_versions():
    # displays the version number of Python, Numpy and OpenCV.
    print "Python's version is " + platform.python_version()
    print "Numpy's  version is " + np.__version__
    print "OpenCV's version is " + cv2.__version__

display_versions()


cam2 = "http://localhost:8090/cam2.mjpeg"
#cam2 = 0 # Use  local webcam.

cam2_mask = cv2.imread(str(os.getcwd()) + "/cam2_mask.png")
if cam2_mask == None:
    print "!!! Couldn't read image cam2_mask.png. CRASH TIME!"
#cv2.imshow('cam2_mask',cam2_mask) #test mask loaded successfuly.
#cam2_mask_dummy = cv2.imread(str(os.getcwd()) + "/cam2_mask_dummy.png")

stream=urllib.urlopen(cam2)
if (stream == None) or (not stream):
    print "!!! Couldn't capture a stream!"

bytes=''
print "Press 'q' to quit."
while True:
    # to read mjpeg frame - 
    bytes+=stream.read(1024)
    #print type(bytes)
    a = bytes.find('\xff\xd8')
    #print "a = " + str(a)
    b = bytes.find('\xff\xd9')
    #print "b = " + str(b)
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        # we now have a mjpeg frame stored in frame.

        masked_frame = cv2.add(frame, cam2_mask)
        #masked_frame = cv2.add(frame, cam2_mask_dummy)

        gray_frame = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
        
        sift = cv2.SIFT()
        kp = sift.detect(gray_frame, None)

        img=cv2.drawKeypoints(gray_frame, kp)

        #cv2.imshow('cam2',masked_frame)
        cv2.imshow('cam2',img)

    # Press q to quit.    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# cam2.release()
cv2.destroyAllWindows()