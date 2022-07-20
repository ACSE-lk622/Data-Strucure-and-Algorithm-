class Bookshelf:
    def __init__(self):
        self.content = [[],[],[]]

    def add_book(self,book,location):
        self.content[location].append(book)
    
    def take_book(self,book,location):
        self.content[location].remove(book)

    def __getitem__(self,location):
        return self.content[location]

my_bookself = Bookshelf()

my_bookself.add_book("Les Miserables",0)
my_bookself.add_book("Pride and Prejudice",0)
my_bookself.add_book("Frankenstein",0)

my_bookself.add_book("Sense and Sensibility",1)
my_bookself.add_book("The little Prince",1)

my_bookself.add_book("Moby Dick",2)
my_bookself.add_book("The adventure of Huckberry",2)
my_bookself.add_book("Dracula",2)
print(my_bookself[1])