from collections import defaultdict 

class Graph :
    def __init__(self,numberofvertices):
        self.graph = defaultdict(list)
        self.numberofvertices = numberofvertices

    def addege(self,vertex, edge):
        self.graph[vertex].append(edge)
    
    def bfs(self,start,end):#O(V+E) BUT V<E SO O(E)
        queue = []
        queue.append([start])
        while queue : #O(V)
            path = queue.pop(0)
            node = path[-1]
            if node == end :
                return path 
            for adjacent in self.gdict.get(node,[]):#O(E)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)