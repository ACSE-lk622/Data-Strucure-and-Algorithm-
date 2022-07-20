class Point2D:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.y + other.y    
        return Point2D(new_x,new_y)

    def __str__(self):
        return f"x = {self.x} , y = {self.y}"
pointA = Point2D(3,4)
print(pointA)
pointB = Point2D(5,6)
print(pointB)
pointC = pointA + pointB
print(pointC)