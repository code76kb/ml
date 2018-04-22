import pygame

SPEED_X =1
SPEED_Y =0
SIZE =20

class Snak:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = SIZE
        self.height = SIZE

    def at(self):
        return  [self.x, self.y, self.height, self.width ]
