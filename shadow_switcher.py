import cv2, platform
import numpy as np


def display_versions():
	# displays the version number of Python, Numpy and OpenCV.
	print "Python's version is " + platform.python_version()
	print "Numpy's  version is " + np.__version__
	print "OpenCV's version is " + cv2.__version__

def random_color():
    # Returns a random integer from 0 to 255
    return np.random.randint(0, 255)

def nothing(x):
    # Returens pass. Needed for the treckbars
    pass

def threshold_limit(orig, threshold, limit):
    # threshold_limit recives orig (int), threshold (int), and limit (int).
    # adds oring and threshold. if the result is above limit the result is clipped.
    # subtracts oring from threshold. if the result is below 0, the result is clipped.
    # returns max_out (int) and min_out (int)
    if (orig + threshold) > limit:
        max_out = limit
    else:
        max_out = orig + threshold

    if (orig - threshold) < 0:
        min_out = 0
    else:
        min_out = orig - threshold

    return max_out, min_out


display_versions()
# start capture
cap = cv2.VideoCapture(0)

#prepare controller window
#def controller_win():
img = np.zeros((300,700,3), np.uint8)
cv2.namedWindow('controller')

# create switch for ON/OFF functionality
switch_text = 'OFF \ ON'
cv2.createTrackbar(switch_text, 'controller', 1, 1, nothing)

# create trackbars for color change.
cv2.createTrackbar('R','controller', 255, 255, nothing)
cv2.createTrackbar('G','controller', 180, 255, nothing)
cv2.createTrackbar('B','controller', 100, 255, nothing)

# Create threshold controllers.
cv2.createTrackbar('Hue Threshold','controller', 0, 179, nothing)
cv2.createTrackbar('Saturation Threshold','controller', 0, 255, nothing)
cv2.createTrackbar('Value  Threshold','controller', 0, 255, nothing)
cv2.createTrackbar('Blur','controller', 0, 25, nothing)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frames
    cv2.imshow('frame', frame)
    cv2.imshow('controller', img)

    # get current positions of trackbars
    r = cv2.getTrackbarPos('R', 'controller')
    g = cv2.getTrackbarPos('G', 'controller')
    b = cv2.getTrackbarPos('B', 'controller')
    s = cv2.getTrackbarPos(switch_text, 'controller')
    hue = cv2.getTrackbarPos('Hue Threshold', 'controller')
    sat = cv2.getTrackbarPos('Saturation Threshold', 'controller')
    val = cv2.getTrackbarPos('Value  Threshold', 'controller')
    blur = cv2.getTrackbarPos('Blur', 'controller')
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
    
    bgr_picker = np.uint8([[[b, g, r]]])
    #print (bgr_picker)
    hsv_picker = cv2.cvtColor(bgr_picker,cv2.COLOR_BGR2HSV)
    #print (hsv_picker[0,0,0])
    hue_max, hue_min = threshold_limit(hsv_picker[0,0,0], hue, 179)
    sat_max, sat_min = threshold_limit(hsv_picker[0,0,1], sat, 255)
    val_max, val_min = threshold_limit(hsv_picker[0,0,2], val, 255)
    

    #lower_blue = np.array([100,50,50])
    #upper_blue = np.array([130,255,255])
    mask_range_max = np.uint8([[[hue_max, sat_max, val_max]]])
    mask_range_min = np.uint8([[[hue_min, sat_min, val_min]]])
    print mask_range_max
    print mask_range_min

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, mask_range_max, mask_range_min)
    cv2.imshow('mask',mask)

    res = cv2.bitwise_and(frame, frame, mask= mask)
    cv2.imshow('res',res)







    # Press 'q' to close windows.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()