import cv2
import numpy as np
import matplotlib.pyplot as plt

path = './Capture.PNG'
window_name = 'HSV'

image = cv2.imread(path)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 160, 255, empty)


while True:
    imgHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask) 
    # mask = 1 (in range)=> giu nguyen gia tri
    # 

    # Histogram
    reduce_mask = mask[int(mask.shape[0]/3*2):,:]/255
    histogram = np.sum(reduce_mask, axis=0)
    print(reduce_mask.shape)
    plt.bar(list(range(0,histogram.shape[0])),histogram)
    print(np.percentile(histogram, [50]))
    # plt.xlabel(range(160, 20))
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([image, mask, result])
    cv2.imshow('Reduced mask', reduce_mask)
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cv2.destroyAllWindows()