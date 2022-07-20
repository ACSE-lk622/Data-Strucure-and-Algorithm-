from collections import defaultdict 

class Graph :
    def __init__(self,numberofvertices):
        self.graph = defaultdict(list)
        self.numberofvertices = numberofvertices

    def addege(self,vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]: #number of edege O(E)
            if i not in visited :
                self.topologicalSortUtil(i,visited,stack)#recursively search in deep
        stack.insert(0,v)
    
    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):# only visit the key of graph,#number of VERTEX O(V+E)
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)#number of edege O(E)
        print(stack)

customgraph = Graph(8)
customgraph.addege("A","C")  
customgraph.addege("C","E")
customgraph.addege("E","H")
customgraph.addege("E","F")
customgraph.addege("F","G")
customgraph.addege("B","D")
customgraph.addege("B","C")
customgraph.addege("D","F")

customgraph.topologicalSort()
