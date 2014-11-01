import cv2, platform
import numpy as np
#import gi.repository

    # mms://194.90.203.111/cam2
    # ffmpeg -i mmst://194.90.203.111/cam2 -f rtsp rtsp://127.0.0.1:
    # ffplay -i mmst://194.90.203.111/cam2
    # E:\Downloads\ffmpeg-20140830-git-596636a-win64-static\bin
    # ffmpeg -i mmst://194.90.203.111/cam2 -ar 44100 -vcodec libx264  -r 25 -b:v 500k -f flv rtmp://127.0.0.1:1935
    # ffmpeg -i mmst://194.90.203.111/cam2 -f flv "rtp://127.0.0.1:1935/cam2"

    
    # vlc http://192.168.0.103:8080/cam2

cam = "mms://194.90.203.111/cam"
#cam = 0 # Use  local webcam.

cap = cv2.VideoCapture(cam)
if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")


while(True):
    # Capture frame-by-frame
    ret, current_frame = cap.read()
    if type(current_frame) == type(None):
        print("!!! Couldn't read frame!")
        break

    # Display the resulting frame
    cv2.imshow('frame',current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()