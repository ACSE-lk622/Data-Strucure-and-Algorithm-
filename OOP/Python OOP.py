class Backpack :

    max = 5
    number = 100
    def __init__(self,number=5 ): #default value , non-default value cannot follow after default parameter
        self.__items = []
        self.max = Backpack.max
        self.number = number
        Backpack.max += 1
    

my_back = Backpack(6)
ur_back = Backpack(7)
print(Backpack.number)
my_back.number = 8
print(my_back.number)
print(my_back.max)
print(ur_back.max)
print(my_back._Backpack__items) #Name mangling which can access non public attribute _classname__attribute
 

