
activity = [["A1",0,6],
            ["A2",3,4],
            ["A3",1,2],
            ["A4",5,8],
            ["A5",5,7],
            ["A6",8,9],
            ]

def printMAXactivity(activity): #TC:O(NlogN) SC:O(1)
    activity.sort(key=lambda x:x[2]) #O(NLOGN)
    i = 0 
    firstA = activity[i][0]
    print(firstA)

    for j in range(len(activity)): #O(N)
        if activity[j][1] > activity[i][2]:
            print(activity[j][0])
            i = j 

printMAXactivity(activity) 