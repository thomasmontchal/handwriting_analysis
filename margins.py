# importing required packages
import cv2 as cv
#margin function with cv.imread parameters and the boundary box dimensiosn for all the text 
def margin(animg):


    # reading the image
    #img = cv.imread(cv.samples.findFile("wics.png"))
    # virat_img = cv.imread(img,0)
    # h, w = virat_img.shape  #gets the size of the image
    img = cv.imread(animg)
    img = cv.imread('threshold1.jpg')
    # convert the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # apply thresholding on the gray image to create a binary image
    ret,thresh = cv.threshold(gray,127,255,0)

    # find the contours
    contours, _ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    x,y,w,h = cv.boundingRect(contours[1]) 
    textBoundary = tuple((x,y,w,h)) 
    margin = ""

    #image border
    top = 0
    bottom = h
    left = 0
    right = w
    verticalCenter_range = 30
    hortizontalCenter_range =30

    #all text border -- this is currentlly an example this should be replaced with an array with the dimensions of a boundary box that contains all text
    topT = textBoundary[1] #y postion of the  boundary box
    bottomT = textBoundary[1]+textBoundary[3] #y+h of the boundary box
    leftT = textBoundary[0] #x of the boundary box
    rightT = textBoundary[0]+textBoundary[2] #x+w of the boundary box

    #chekc location of text border
    if((top- topT)-(bottom- bottomT) > verticalCenter_range): # if te text is not within range of the vertical center 
        if((top- topT) > (bottom- bottomT) ): # then check if the text is closet to the bottom
                margin = "bottom-"
        elif((top- topT) < (bottom - bottomT)): #also check if the text is closer to the top
                margin = "top-"
    elif((top- topT)-(bottom- bottomT) <= verticalCenter_range):
        margin = "center-"

    if((left- leftT)-(right- rightT) > hortizontalCenter_range):  # if te text is not within range of the horizontal center 
        if((left- leftT)>(right- rightT)): # then check if the text is closet to the right
                margin += "right"
        elif((left- leftT)<(right- rightT)): # also check if the text is closer to the left
                margin += "left"
    elif((left- leftT)-(right- rightT) <= hortizontalCenter_range):
        margin += "center"
    #read bordes values from file

    # making border around image using copyMakeBorder
    borderoutput = cv.copyMakeBorder(virat_img,10, 10, 10, 10, cv.BORDER_CONSTANT,value=0)

    # showing the image with border
    cv.imwrite('output.png', borderoutput)
    #cv.imshow("Display window", borderoutput)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    return margin