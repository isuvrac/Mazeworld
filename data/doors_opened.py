# Count number of doors opened
import csv
import numpy as np
file = open('data.csv')
csvreader = csv.reader(file)
count = []
for row in csvreader:
    for column in row:
        if "Doors1_Open:" in column:
            x = column.split(":")
            if x[1] == 'True':
                count.append(1)
            else:
                count.append(0)
file.close()
print("Door_1 was opened:", np.count_nonzero(np.diff(count)), "Time")

# print specified column
import csv
tag = "Player_Tactical_1002_Position_X:"
file = open('data.csv')
csvreader = csv.reader(file)
for row in csvreader:
    for column in row:
        if tag in column:
            # # Print just the data
            # x = column.split(":")
            # print(x[1])

            # Print the entire line
            print(column)
file.close()
