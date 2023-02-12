import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def evaluateBaseLine(anImg):
    # Read image from which text needs to be extracted
    # path = 'C:\\Users\\bayme\\OneDrive\\Documents\\opencv\\test.jpg'
    path = anImg
    img = cv.imread(path, 0)

    # Preprocessing the image by blurring it and finding the edges
    blurred = cv.GaussianBlur(img,(5,5),0) 
    edged = cv.Canny(blurred, 30, 150)

    # Finding the contours
    contours, hierarchy = cv.findContours(edged, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # taking the first contour to be our starting value to judge the baseline
    cnt = contours[0]
    x, y, w, h = cv.boundingRect(cnt)
    maxX = 0
    firstX = x
    firstY = y
    firstH = h
    firstW = w
    rect = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # list to hold our deviations from the baseline
    deviations = [] 

    # looping through the contours to find the last contour
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        if((x > maxX) and ( (y < (firstY + 15)) and (y > (firstY -15)) )):
            maxX = x
            maxW = w

    # finding the deviation between the baseline and the rest of the letters 
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        if((y < (firstY + 15)) and (y > (firstY -15)) ):
            deviations.append(((firstY) - (y)))
            deviations.append(((firstY+firstH) - (y+h)))
            #rect = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # if positive avg of the deviation that means it went upwards
    # if negative avg of the deviation that mean it went downwards
    # print(sum(deviations) / len(deviations))
    if ((sum(deviations) / len(deviations))>0):
        return "Slanted Upwards"
    return "Slanted Downwards"

    #return (sum(deviations) / len(deviations))
    # # visualing the baseline
    # cv.line(img, tuple((firstX, firstY+firstH)), tuple(( (maxX + maxW), (firstY+firstH))),(0,255,0),2)
    # cv.imshow("Bounding Rectangle", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

# test code to make the bounding box
#rect = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)