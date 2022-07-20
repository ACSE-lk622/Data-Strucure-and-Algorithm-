#id() return the address of the object in memory
# "is" , return true when reference the same object
# ""=="", return true when two object has the same value 

# for list has different critiria in "=="
print(id(15))

a = -7
b = -7

print(a is b)
print(a == b)
print(hash(a))
print(id(a))
print(id(b))
class Dog :
    def __init__(self,items):
        self.item = items 


dog1 = Dog(5)
dog2 = Dog(5)

print(hash(dog1))




a = [2,5,3,53]

def print_data(seq):
    print(id(seq))
    for ele in seq:
        print(ele)
print(id(a))
print_data(a)


def double_data(seq):
    print(id(seq))
    for ele in range(len(seq)):
        seq[ele] *= 2 

print(id(a))
double_data(a)
print(a)


class List :
    def __init__(self, amount):
        self.amount = amount 

    def Total_list(seq):
        total = 0 

        for ele in seq :
            total += ele.amount
        return total

Sale_list = [List(450),List(350),List(50)]
print(List.Total_list(Sale_list))



# this will error , due to the change of size of dictionary during iteration.
# can solve by cloning  , for key,value in dictionary.copy().items()
def remove_even_values(dictionary):
    for key ,value in dictionary.items():
        if value % 2 == 0 :
            del dictionary[key]
mydic = {"a":1,"b":2,"c":3,"d":4}
remove_even_values(mydic)



# default arguments are initialized when the methods are initially processed.
class WaitingList:
	
	def __init__(self, clients=[]):
		self.clients = clients
		print("List id:", id(self.clients))
		
	def add_client(self, client):
		self.clients.append(client)
 
		
waiting_list1 = WaitingList()
waiting_list2 = WaitingList()


# use none as default argument 
class WaitingList1:
	
    def __init__(self, clients=None):
        if clients == None:
            self.clients = []
        else:
            self.clients = clients		
    def add_client(self, client):
	    self.clients.append(client)

