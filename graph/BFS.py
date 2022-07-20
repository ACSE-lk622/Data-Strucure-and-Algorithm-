class Graph :
    def __init__(self):
        self.gdict = {
    'A': ["B", "D", "E"],
    'B': ["A", "C"],
    'C': ["B", "E"],
    'D': ["A", "E"],
    'E': ["A", "D", "F", "C"],
    'F': ["E"]     
}
    def addedge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False 
    def bfs(self,vertex): #TC :O(V+E) SC : O(V+E)
        visited  = [vertex]
        queue = [vertex]
        while queue : # TC:O(V) , V = number of vertex 
            devertex = queue.pop(0)
            print(devertex)
            for adjacentvertex in self.gdict[devertex]: #O(N) , N = number of edges 
                if adjacentvertex not in visited :
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)
    def dfs(self,vertex):#TC :O(V+E) SC : O(V+E) if V>E will be O(V) else O(E)
        visited = [vertex]
        stack = [vertex]
        while stack : #TC:O(V)
            devertex = stack.pop()
            print(devertex)
            for adjacentvertex in self.gdict[devertex]: #TC:O(E)
                if adjacentvertex not in visited :
                    visited.append(adjacentvertex)  
                    stack.append(adjacentvertex)
gragh = Graph()
gragh.dfs("A")