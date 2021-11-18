
# count number of doors opened
# importing necessary libraries
import csv
import numpy as np

# array with a value for each door in the maze
doorArray = [1,2,3,4,5,6,7,8,9]
# array for output values
outputArray = []

# for loop that goes through each value in doorArray
for value in doorArray :
    
    # openning file and getting ready to read it
    file = open('team6.csv')
    csvreader = csv.reader(file)
    
    # turns true and false values into binary 
    count = []
    for row in csvreader:
        for column in row:
            if "Doors"+str(value)+"_Open:" in column:
                x = column.split(":")
                if x[1] == 'True':
                    count.append(1)
                else:
                    count.append(0)
                    
    # closing file
    file.close()
    
    # counts how many times there is a change between 0 and 1 (true and false)
    outputArray.append("Door_" + str(value) + " was opened: " + str(np.count_nonzero(np.diff(count)))+ " Times")

# prints how many time each door was openned during the trial 
for out in outputArray:
    print(out)