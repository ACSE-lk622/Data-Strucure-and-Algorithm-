# Property function :  do not need to change name of instance attribute when use non public attritube 


class Dog :
    def __init__(self, age):
        self._age = age 
    def get_age(self):
        print("This is get ")
        return self._age
    def set_age(self,new_age):
        print("This is set ")
        self._age = new_age
        

    age = property(get_age,set_age)

my_dog = Dog(8)
print(my_dog.age) # call get 
my_dog.age = 9  # call set 
print(my_dog.age) # call get 