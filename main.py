print("-----Alphabetical Pattern-----")
for x in range(65,69): #ASCII Value of A to D = 65 to 69
    for j in range(65,x+1): #Increment until the prev. value of the max. value
        print(chr(x),end="") #Print the output
    print()#Print in new line
