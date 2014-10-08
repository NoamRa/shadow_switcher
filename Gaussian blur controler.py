import cv2, platform
import numpy as np
#from matplotlib import pyplot as plt


def display_versions():
	# displays the version number of Python, Numpy and OpenCV.
	print "Python's version is " + platform.python_version()
	print "Numpy's  version is " + np.__version__
	print "OpenCV's version is " + cv2.__version__

def nothing(x):
    # Returens pass. Needed for the treckbars
    pass

def make_odd(num):
    if num == 0:
    	return none
    elif num % 2 == 0:
    	return num -1
    else:
    	return num

display_versions()
# start capture
cap = cv2.VideoCapture(0)

img = np.zeros((300,700,3), np.uint8)
cv2.namedWindow('controller')

cv2.createTrackbar('Blur','controller', 1, 20, nothing)



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Display the resulting frames
    
    cv2.imshow('controller', img)

    blur = cv2.getTrackbarPos('Blur', 'controller')
    if blur == 0:
    	cv2.imshow('frame', frame)
    elif blur % 2 == 0:
    	blur = blur -1
    	frame = cv2.GaussianBlur(frame, (blur, blur), 0)
    	cv2.imshow('frame', frame)
    else: 
    	frame = cv2.GaussianBlur(frame, (blur, blur), 0)
    	cv2.imshow('frame', frame)
    	
    

    



    







    # Press 'q' to close windows.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()