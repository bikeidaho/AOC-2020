import numpy as np

input = open('.\Day2\day2-input.txt')
listofpasswords = input.read().splitlines()

list = np.asarray(listofpasswords)
initialcount = 0

print("Initial Count = " +str(initialcount))
for item in listofpasswords:
    compare = item.split()
    letter = compare[1].replace(':','')
    
    range = compare[0]
    rangedelimited = range.replace('-', ' ')
    rangesplit = rangedelimited.split()
    
    password = compare[2]
    first = rangesplit[0]
    second = rangesplit[1]
   
    print("Password " +password)
    print("First Pos " +first)
    print("Second Pos " +second)
    
    print("Searching for " +letter)
    
    firstpos = password[int(first)-1]
    secondpos = password[int(second)-1]
    print("First letter " +firstpos)
    print("Second letter " +secondpos)

    if firstpos == letter and secondpos != letter:
        initialcount +=1
    elif firstpos != letter and secondpos == letter:
        initialcount +=1        
    print(initialcount)
