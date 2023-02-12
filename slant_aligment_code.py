import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math


# Read image from which text needs to be extracted
path = 'C:\\Users\\bayme\\OneDrive\\Documents\\opencv\\test3.jpg'
img = cv.imread(path, 0)

# Preprocessing the image by blurring it and finding the edges
blurred = cv.GaussianBlur(img,(5,5),0) 
edged = cv.Canny(blurred, 30, 150)

# Finding the contours
contours, hierarchy = cv.findContours(edged, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Counter for the total of right/left aligment letters
right_aligment_counter = 0
left_aligment_counter = 0

# make a rotated bounding border
for cnt in contours:
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int64(box)
    cv.drawContours(img,[box],0,(0,0,255),2)

    # get the imporant points of the rotated boxes
    x1 = (box[0])[0]
    y1 = (box[0])[1]

    x2 = (box[1])[0]
    y2 = (box[1])[1]

    x4 = (box[3])[0]
    y4 = (box[3])[1]


    # find the distance of the edges of left most point and the top point and the distance of the 
    # edge of the left most point and bottom point using the distance formula 
    d = math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))
    e = math.sqrt( ((x4 - x1)**2) + ((y4 - y1)**2))

    # if the left most point and the top point is the larger edge than it means it is right leaning
    if(d > e):
        right_aligment_counter += 1
    
    
    # if the left most point and the bottom point is the larger edge than it means it is left leaning
    if(e > d):
        left_aligment_counter += 1


 # if there is more right leaning letter therefore it is a right leaning word
if(right_aligment_counter > left_aligment_counter):
    print("right")

 # if there is more left leaning letter therefore it is a left leaning word
if(right_aligment_counter < left_aligment_counter):
    print("left")

# if there equal of left leaning and right leaning letters than the word aligned
if(right_aligment_counter == left_aligment_counter):
    print("aligned")

cv.imshow("rotated", img)
cv.waitKey(0)
cv.destroyAllWindows()