class Polygon:
    def __init__(self,num_sides,color):
        self.num_sides = num_sides
        self.color = color 

class Triangle(Polygon):
     # if subclass no __init__ , it will inherit superlclass __init__ , if subclass has its own init , need to define superclass init in side 
    NUM_SIDES = 3 
    def __init__(self,base=0,height=5,color="blue"):
        Polygon.__init__(self,Triangle.NUM_SIDES,color) #super().__init__(Triangle,NUM_SIDES,color)
        self.base = base 
        self.height = height  

Tri = Triangle()
print(Tri.base)
print(Tri.color)
print(Tri.num_sides)
class Character:

    def __init__(self,x,y,num_lives):
        self.x = x 
        self.y = y 
        self.num_lives = num_lives
class Player(Character):
    
    INITIAL_X = 0 
    INITIAL_Y = 0 
    INITIAL_NUM_LIVES = 10   

    def ___init__(self,score=0):
        super().__init__(self,Player.INITIAL_X,Player.INITIAL_Y,Player.INITIAL_NUM_LIVES)
        self.score = score 
class Enemy(Character):
    def __init__(self,x=15,y=15,num_lives=8,is_poisonous=False):
        Character.__init__(self,x,y,num_lives)
        self.is_poisonous = is_poisonous
player = Player()
print(player.x)
easy_enemy = Enemy(num_lives=1)
print(easy_enemy.is_poisonous)
print(easy_enemy.x)
print(easy_enemy.y)
print(easy_enemy.num_lives)



class Sprite:
    
	def __init__(self, x, y, img_file, speed, life_counter):
		self.x = x
		self.y = y
		self.img_file = img_file
		self.speed = speed
		self.life_counter = life_counter
 
class Enemy(Sprite):
    
	def __init__(self, x, y, img_file, speed,life_counter=5):
	    Sprite.__init__(self, x, y, img_file, speed, life_counter)
	    self.message = "I'm here to protect my master"
 
class Player(Enemy):
    
	def __init__(self, x, y, img_file, speed):
		Sprite.__init__(self, y, img_file, speed, 6)
		self.speed = 56
 
class DifficultEnemy(Enemy):
    
	def __init__(self, x, y, img_file):
		Enemy.__init__(self, img_file, 80)
 
class EasyEnemy(Enemy):
    
	def __init__(self, x, y, img_file):
            Enemy.__init__(self, x, y, img_file, 40)
		