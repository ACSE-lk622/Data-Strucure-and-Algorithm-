class Graph :
    def __init__(self):
        self.gdict = {}

    def addvertex(self,vertx):
        if vertx not in self.gdict.keys():
            self.gdict[vertx] = []
            return True
        return False 

    def addedge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False 
    def remove_edge(self,vertex1,vertex2):
         if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try:
                self.gdict[vertex1].remove(vertex2)
                self.gdict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True

    def printgraph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])
graph = Graph()
graph.addvertex("a")
graph.addvertex("b")
graph.addvertex("c")
graph.addvertex("d")
graph.addedge("b","a")
graph.addedge("b","c")
graph.addedge("c","a")
graph.printgraph()
graph.remove_edge("a","d")
