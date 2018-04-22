
import random

SIZE = 20

class Food:

     def __init__(self):

         self.x  = random.randint(0,580/SIZE)*SIZE
         self.y  = random.randint(0,580/SIZE)*SIZE
         self.width = SIZE
         self.height = SIZE

     def at(self):
         return [ self.x, self.y , self.height, self.width]
