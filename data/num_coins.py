# Number of Coins Collected Total
def cointCoins(File):
    with open(File,'r') as file: 
        data = file.readlines() 
    lastRow = data[-1] 

    tag = "_Collected:"
    counter = 0

    for cellData in lastRow.split(","):
        if tag in cellData:
            if 'True' in cellData:
                counter = counter + 1
    print(counter)