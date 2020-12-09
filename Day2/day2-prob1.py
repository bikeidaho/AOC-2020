import numpy as np

input = open('.\Day2\day2-input.txt')
listofpasswords = input.read().splitlines()

list = np.asarray(listofpasswords)
intitialcount = 0

for item in listofpasswords:
    compare = item.split()
    lettercount = compare[2].count(compare[1].replace(':',''))
    
    range = compare[0]
    rangedelimited = range.replace('-', ' ')
    rangesplit = rangedelimited.split()
    
    low = rangesplit[0]
    high = rangesplit[1]
   
    if int(low) <= lettercount  <= int(high):
        intitialcount +=1 
        print(intitialcount)
    
    
    

