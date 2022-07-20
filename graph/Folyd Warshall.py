

INF = 9999
#Printing Solution 

def printSoltion(nV,distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j]== INF ):
                print("INF",end = " ")
            else:
                print(distance[i][j],end=" ")
        print(" ")

def FloydWarshall(nV,G): #TC:O(V^3),SC:O(V^2)
    distance = G # to not influence initial graph 
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j]= min(distance[i][j],distance[i][k]+distance[k][j]) # if direct distance is bigger than indirect distance , detch smaller distance 
    
    printSoltion(nV,distance)