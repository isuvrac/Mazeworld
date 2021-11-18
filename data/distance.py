# count number of doors opened
# importing necessary libraries
import csv
import numpy as np

# openning file and getting ready to read it
file = open('team9.csv')
csvreader = csv.reader(file)

# local variables that store data about the position of the two players
dist = []
collectorPosX = []
collectorPosY = []
explorerPosX = []
explorerPosY = []

# loop to get data out of the csv file
for row in csvreader: 
    for column in row:
        
        # finding section and adding coordinates to a specific list
        if "2002_Position_X:" in column:
            cPosX = column.split(":")
            collectorPosX.append(float(cPosX[1]))
        if "2002_Position_Y:" in column:
            cPosY = column.split(":")
            collectorPosY.append(float(cPosY[1]))
        if "3002_Position_X:" in column:
            ePosX = column.split(":")
            explorerPosX.append(float(ePosX[1]))
        if "3002_Position_Y:" in column:
            ePosY = column.split(":")
            explorerPosY.append(float(ePosY[1]))


# takes the four different lists and vectorizes them in order to get distance
count = 0

while count < len(collectorPosX):
    dist.append(np.sqrt((collectorPosX[count]-explorerPosX[count])**2+(collectorPosY[count]-explorerPosY[count])**2)) 
    count+= 1        
                     
file.close()

# this section allows for specific data to be output
print(np.std(dist))
    