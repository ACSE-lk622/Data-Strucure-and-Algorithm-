class Circle :
    def __init__ (self, raduis):
        self.radius = radius
    
    def find_diameter(self,     ):
        print(f"Diameter: {self.radius * 2 }")

class Backpack : 
    def __init__(self):
        self._items = []

    @property 
    def items(self):
        return self._items

    #use method A in method B 
    def muladd_items(self,items):
        for item in items :
            self.add_items(item)
    def add_items(self, item):
        if isinstance(item, str ):
            self._items.append(item)
    def remove_item(self,item):
        if item in self._items :
            self._items.remove(item)
            return 1 
        else :
            return 0 
    def has_item(self,item):
        return item in self._items 
    #Sorted list by True or False 
    def show_items(self,sorted_list = False):
        if sorted_list :
            print(sorted(self._items))
        else :
            print(self._items)
mybackpack = Backpack()
mybackpack.add_items("Wanting")
mybackpack.add_items("Tina")
mybackpack.add_items("Losfre")
mybackpack.show_items()
mybackpack.show_items(True)
mybackpack.muladd_items(["Curtis","Kennny","Parry"])
print(mybackpack.items)
mybackpack.remove_item("Parry")

