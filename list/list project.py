numDays = int(input("How many day's temperature ? "))

total = 0 
temp = []

for i in range(numDays):
    nextDays = int(input("Day "+ str(i+1) +  "'s high temperature : "))
    temp.append(nextDays)
    total = total + temp[i]

avg = round(sum(temp)/numDays)
print("\nAverage = " + str(avg))

above = 0 

for i in temp :
    if i > avg :
        above += 1
print(str(above) + " day(s) above average ")