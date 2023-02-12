def zoning(borders):
    borders = [] #2d array for all charater's boundary box dimensions 
    #zones = [] #array of zone results
    upperZoneCount = 0
    bottomZoneCount = 0
    middleZoneCOunt = 0

    baseline = borders[0][1] + borders[0][3] #baseline of first character - assuming that the first character in the sentence is gong to be a capital letter
    topZoneLine = (borders[0][3]+borders[0][1])/2 #centerline of first charracter used as line to jusge zones
    #reads in the handwritting border dimensions and compares if they are within range
    for valueArray in borders:  
        if(valueArray[1] < topZoneLine): #if top of the boundary box is above the zone line than the letter is within in the upper zone
            #zones.append("U") 
            upperZoneCount+=1
        elif(valueArray[1] > baseline): #if the  botttom of the noundary box is below the baseline the leter is within the  bottom zone
            #zones.append("B")
            bottomZoneCount+=1
        else:                           #otherwise if non of the other conditions are met thaan the letter is within the middle zone
            #zones.append("M") 
            middleZoneCOunt +=1
    return upperZoneCount,bottomZoneCount, middleZoneCOunt
