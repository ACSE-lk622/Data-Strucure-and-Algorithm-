class Movie :
    def __init__(self, title, rating ):
        self._title = title
        self.rating = rating 
    def get_title(self):
        return self._title

class Dog:
    def __init__(self, name, age):
        self._name = name
        self.age =age 
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else :
            print("Please enter a valid name ")

class Backpack :
    def __init__(self):
        self._items = []
    def get_items(self):
        return self._items
    def set_items(self, new_items):
        if isinstance(new_items,list):
            self._items = new_items 
        else :
            print("Please enter a valid list of items")
class Circle :
    def __init__(self,radius):
        self._radius = radius
    def get_radius(self):
        return self._radius
    def set_radius(self,new_radius):
        if isinstance(new_radius,float) and new_radius > 0:
            self._radius =new_radius
        else :
            print("Please enter a valid value ")
my_circle = Circle(5.0)
print(my_circle.get_radius())
my_circle.set_radius(10.5)
print(my_circle.get_radius())
my_backpack = Backpack()
print(my_backpack.get_items())
my_backpack.set_items(["Water Bottle","Sleeping Bag", "First Aid Kit"])
print(my_backpack.get_items())

my_movie = Movie("The Godfather",4.8)
print(my_movie.get_title())

my_dog = Dog("Nora",8)
print("My dog is : ",my_dog.get_name())
my_dog.set_name("Norita")
print("Her new name is ", my_dog.get_name())