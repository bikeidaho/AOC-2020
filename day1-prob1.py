import numpy as np

input = open('day1-prob1-input.txt', 'r')
listofnumbers = input.read().split()

solution = 2020

list = np.asarray(listofnumbers)

for item1 in range(0,len(list)):
    for item2 in range(0,len(list)):
        sumnum = int(list[item1]) + int(list[item2])
        if sumnum == solution:
                print("Number 1: " + list[item1] + " Number 2: " + list[item2])
                answer = int(list[item1]) * int(list[item2])
                print("Answer is: " + str(answer))
        
            
        