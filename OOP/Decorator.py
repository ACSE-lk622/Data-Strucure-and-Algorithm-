#Decorator : can use decorator property to replace get function for non public attribute 

class Movie: 
    def __init__(self,title,rating):
        self.title = title 
        self._rating = rating 

    @property
    def rating(self):
        print("this is decorator")
        return self._rating
    @rating.setter
    def rating(self, new_rating):
        print("call setter")
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0 :
            self._rating = new_rating 


favorite_movie = Movie("Titanic",4.3)
print(favorite_movie.rating)
favorite_movie.rating = 4.5 
print(favorite_movie.rating )