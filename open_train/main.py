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

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

cam2 = "http://localhost:8090/cam2.mjpeg"
#cam2 = 0 # Use  local webcam.

# get mask
cam2_mask = cv2.imread(str(os.getcwd()) + "/cam2_mask.png")
if cam2_mask == None:
    print "!!! Couldn't read image cam2_mask.png. CRASH TIME!"

# get stream
global stream
stream=urllib.urlopen(cam2)
if (stream == None) or (not stream):
    print "!!! Couldn't capture a stream!"

global bytes
bytes=''
print "Press 'q' to quit."

def make_frame(bytes):
    out_frame = None
    while out_frame != None:
        # to read mjpeg frame - 
        bytes+=stream.read(1024)
        a = bytes.find('\xff\xd8')
        print a
        b = bytes.find('\xff\xd9')
        print b
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            out_frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
            # we now have a mjpeg frame stored in frame.
        else: 
            print "SOMETHING'S WRONG WITH MAKE_FRAME()!"
    return out_frame

while True:
    frame = make_frame(bytes)
    #masked_frame = cv2.add(frame, cam2_mask)
    
    cv2.imshow('cam2',frame)

    # Press q to quit.    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# cam2.release()
cv2.destroyAllWindows()