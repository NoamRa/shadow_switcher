import cv2, platform
import numpy as np
import urllib


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
#cam = 0 # Use  local webcam.

stream=urllib.urlopen(cam2)
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('cam2',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()