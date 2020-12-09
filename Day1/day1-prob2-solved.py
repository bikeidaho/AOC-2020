import numpy as np

input = open('.\Day1\day1-input.txt', 'r')
listofnumbers = input.read().split()

solution = 2020

list = np.asarray(listofnumbers)

for item1 in range(0,len(list)):
    for item2 in range(0,len(list)):
        for item3 in range(0,len(list)):
            sumnum = int(list[item1]) + int(list[item2]) + int(list[item3])
            if sumnum == solution:
                    print("Number 1: " + list[item1] + " Number 2: " + list[item2] + " Number 3: " + list[item3])
                    answer = int(list[item1]) * int(list[item2]) *int(list[item3])
                    print("Answer is: " + str(answer))
        
            
        