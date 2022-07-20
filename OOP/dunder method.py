from tkinter import Y


print(5+6)
result = 5 + 6
result = (5).__add__(6)
print((5).__add__(6))
mystring = [5,2,3,4]
print(len(mystring))
print(mystring.__len__())

class Point2D :
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def __str__(self):
        return f"({self.x},{self.y})"

mypoint = Point2D(56,60)
print(mypoint)

class Backpack:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        if item in self.items :
            self.items.remove(item)
        else :
            print("This item is not in the backpack.")
    def __len__(self):
        return len(self.items)

my_backpack = Backpack()
my_backpack.add_item("Water bottle")
my_backpack.add_item("Losfre")
my_backpack.add_item("Sleeping bag")
print(len(my_backpack))