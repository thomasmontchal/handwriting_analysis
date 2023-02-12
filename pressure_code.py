# import the cv2 library
import cv2
import numpy as np
import matplotlib.pyplot as plt

def imThreshold(img, threshold, maxVal):
    assert len(img.shape) == 2 # input image has to be gray
    
    height, width = img.shape   # getting image dimension
    bi_img = np.zeros((height, width), dtype=np.uint8)      # creating a matrix of image size filled with zeros
    for x in range(height):
        for y in range(width):
            if img.item(x, y) > threshold:
                bi_img.itemset((x, y), maxVal)              # If pixel intensity > threshold, set to 255, otherwise 0
                
    return bi_img

#anImg should be a string/path to an image
def evaluatePressure(anImg):
    # The function cv2.imread() is used to read an image.
    my_img = cv2.imread(anImg,0) #0 means no color, 1 means color, -1 means unchanged
    cv2.imwrite('grayscale.jpg',my_img)
    new_img = imThreshold(my_img,155,255) 
    # The function cv2.imshow() is used to display an image in a window.
    thresholds =[50,100,155,200]

    img = cv2.imread(anImg)


    # convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply thresholding on the gray image to create a binary image
    ret,thresh = cv2.threshold(gray,127,255,0)

    # find the contours
    contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # take the first contour
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        img = cv2.drawContours(img,[contour],0,(0,255,255),2)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # cv2.imshow("Bounding Rectangle", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    # cv2.imshow("Bounding Rectangle", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    white=[]
    black=[]

    for threshold in thresholds:
        histw= 0
        histb= 0
        #img=cv2.threshold(gray, threshold, 255,0)
        img = imThreshold(gray,threshold,255)
        height, width = img.shape
        for x in range(height):
            for y in range(width):
                if img.item(x,y) == 255:
                    histw = histw+1
                
                else:         
                    histb+=1
        
        print("Threshold: ", threshold)
        # plt.imshow(img, cmap='gray')

        plt.show()

                    
        white.append(histw)
        black.append(histb)
        
        
    
    print("The white array is: ", white)
    print("The black array is: ", black)

    count=0
    sum=0
    mean=0

    m=[0,1,2,3]

    for i in m: 
        if(black[i]>10000):
            count+=1 
        sum=sum+black[i]

    mean=sum/4
    percent=0
    print(mean)
    print(count)

    if count==4: 
        # print("Proper Pressure")
        return "Proper Pressure" 

    if mean>10000: 
        # print('Proper Pressure')
        return "Proper Pressure"
    else: 
        percent=(10000-mean)/100
        # print('Your writing needs to be ', percent, 'percent thicker to qualify for proper pressure/ clarity threshold')
        return 'Your writing needs to be '+ str(percent) + 'percent thicker to qualify for proper pressure/ clarity threshold'



                    



    # cv2.imshow('threshold image',new_img)
    # waitKey() waits for a key press to close the window and 0 specifies indefinite loop
    # cv2.waitKey(0)
    
    # cv2.destroyAllWindows() simply destroys all the windows we created.
    # cv2.destroyAllWindows()
    
    # The function cv2.imwrite() is used to write an image.
    # cv2.imwrite('threshold.jpg',new_img)