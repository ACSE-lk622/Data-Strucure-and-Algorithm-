class Circle:
    def __init__(self,radius,color):
        self.radius = radius 
        self.color = color  

    def __lt__(self,other): # obj1 < obj2 
        return self.radius < other.radius 

    def __le__(self, other): 
        return self.radius <= other.radius

    def __gt__(self,other):
        return self.radius > other.radius 
    
    def __ge__(self,other):
        return self.radius >= other.radius 

    def __eq__(self,other):
        return (self.radius == other.radius and self.color == other.color)
    
    def __ne__(self,other):
        return (self.radius != other.radius or self.color != other.color )

circleA = Circle(5,"Blue")
circleB = Circle(5,"Green")
circleC = Circle(7,"Red")
circleD = Circle(5,"Blue")

print(circleA  <= circleB)