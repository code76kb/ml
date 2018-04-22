from Snak import Snak
from Nural_Net import Nural_Net
import numpy as np
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
SIZE = 20

WIDTH = 600.000
HEIGHT =600.000
FView = 10

def sigmoid(x):
    return 1 / (1 + np.e ** -x)

class Full_Snake:

    def __init__(self,snaklen):
            self.SPEED_X =random.randint(0,1)
            self.SPEED_Y = 1 - self.SPEED_X
            self.snak_len = snaklen
            self.snake_body = [None]*self.snak_len
            for i in xrange(0,self.snak_len):
                if i==0:
                    self.snake_body[i]=Snak (random.randint(0,580), random.randint(0,580))
                else:
                    self.snake_body[i]=Snak (self.snake_body[i-1].x-SIZE,self.snake_body[i-1].y)



            self.s_Color = (random.randint(1,250), random.randint(5,255), random.randint(10,245))

            self.nural_Net = Nural_Net()
            self.fitness=1
            self.isAlive=True

            self.dis_up = 0
            self.dis_down = 0
            self.dis_left = 0
            self.dis_right = 0
            self.dis_food = 0
            self.dis_x_food = 0
            self.dis_y_food = 0



    def initiaze_network(self):
        self.nural_Net.create_Weight_Martix()


    def get_nxt_move(self,input_vector):
        self.nural_Net.input_vector = input_vector
        output_vec = self.nural_Net.feed_forward()
        output = np.argmax(output_vec)
        # print('\n output vec:',output_vec)
        # [left, top ,right ,bottom]

        #left, ahead, right


        # if output == 0:        # left
        #     self.SPEED_X = -1
        #     self.SPEED_Y = 0
        # if output == 1:        # top
        #     self.SPEED_X = 0
        #     self.SPEED_Y = -1
        # if output == 2:        # Right
        #     self.SPEED_X = 1
        #     self.SPEED_Y = 0
        # if output == 3:        # bottom
        #     self.SPEED_X = 0
        #     self.SPEED_Y = 1

        # print("output_vec::",output_vec,"\n max at:",output)
        # print("Dire :X",self.SPEED_X," \n Y:",self.SPEED_Y)



    def update_pos(self):

                for i in xrange(self.snak_len,0,-1): ## update individual snake pos

                    if i-1 != 0:
                       self.snake_body[i-1] = self.snake_body[i-2]
                    else:
                       self.snake_body[i-1] = Snak(self.snake_body[i-1].x+(self.SPEED_X*SIZE), self.snake_body[i-1].y+(self.SPEED_Y*SIZE))

                    # Move through walls

                    if self.snake_body[i-1].x > WIDTH:
                        self.snake_body[i-1].x = 0

                    if self.snake_body[i-1].x<0:
                        self.snake_body[i-1].x = WIDTH

                    if self.snake_body[i-1].y  > HEIGHT:
                        self.snake_body[i-1].y = 0

                    if self.snake_body[i-1].y < 0:
                        self.snake_body[i-1].y = HEIGHT

    def bite(self):

          for i in xrange(1,self.snak_len):

               #get view
               #Left
               if (self.snake_body[0].x - FView <= self.snake_body[i].x and self.snake_body[0].x >= self.snake_body[i].x and  self.snake_body[0].y == self.snake_body[i].y):
                   self.dis_left = np.sqrt(np.power((self.snake_body[0].x - self.snake_body[i].x),2) + np.power((self.snake_body[0].y - self.snake_body[i].y),2))
                   # normalizing in range on 0-1
                   self.dis_left = self.dis_left / (FView*SIZE)
               elif True: #(self.snake_body[0].x <= FView*SIZE):
                    self.dis_left = np.sqrt(np.power((self.snake_body[0].x - 0),2) + np.power((self.snake_body[0].y - self.snake_body[0].y),2))
                    self.dis_left = (self.dis_left / WIDTH )
                    # print("\n dL:", self.dis_left)


               # Right
               if (self.snake_body[0].x + FView >= self.snake_body[i].x and self.snake_body[0].x <= self.snake_body[i].x and  self.snake_body[0].y == self.snake_body[i].y):
                   self.dis_right = np.sqrt(np.power((self.snake_body[0].x - self.snake_body[i].x),2) + np.power((self.snake_body[0].y - self.snake_body[i].y),2))
                   # normalizing in range on 0-1
                   self.dis_right = self.dis_right / (FView*SIZE)

               elif True: #WIDTH -self.snake_body[0].x <= FView*SIZE):
                    self.dis_right = np.sqrt(np.power((WIDTH - self.snake_body[i].x),2) + np.power((self.snake_body[0].y - self.snake_body[0].y),2))
                    self.dis_right = self.dis_right / WIDTH#(FView*SIZE)
                    # print("\n dR:", self.dis_right)


               # Up
               if (self.snake_body[0].y - FView <= self.snake_body[i].y and self.snake_body[0].y >= self.snake_body[i].y and  self.snake_body[0].x == self.snake_body[i].x):
                   self.dis_up = np.sqrt(np.power((self.snake_body[0].x - self.snake_body[i].x),2) + np.power((self.snake_body[0].y - self.snake_body[i].y),2))
                   # normalizing in range on 0-1
                   self.dis_up = self.dis_up / FView*SIZE
               elif True: #self.snake_body[0].y <= FView*SIZE :
                   self.dis_up = np.sqrt(np.power((self.snake_body[0].y - 0),2) + np.power((self.snake_body[0].x - self.snake_body[0].x),2))
                   self.dis_up = self.dis_up / HEIGHT
                   # print("\n dU:", self.dis_up)


               #Down
               if (self.snake_body[0].y + FView >= self.snake_body[i].y and self.snake_body[0].y <= self.snake_body[i].y and  self.snake_body[0].x == self.snake_body[i].x):
                   self.dis_down = np.sqrt(np.power((self.snake_body[0].x - self.snake_body[i].x),2) + np.power((self.snake_body[0].y - self.snake_body[i].y),2))
                   # normalizing in range on 0-1
                   self.dis_down = self.dis_down / (FView*SIZE)
               elif True:#HEIGHT-self.snake_body[0].y <= FView*SIZE:
                   self.dis_down = np.sqrt(np.power((self.snake_body[0].x - self.snake_body[0].x),2) + np.power((HEIGHT - self.snake_body[0].y),2))
                   self.dis_down = self.dis_down / HEIGHT#(FView*SIZE)
                   # print("\n dD:", self.dis_down)


               ####
               dis = np.sqrt(np.power((self.snake_body[0].x - self.snake_body[i].x),2) + np.power((self.snake_body[0].y - self.snake_body[i].y),2))
               if dis < 1:
                  print("MArgya Chutiya!!!")
                  self.snake_body = [Snak(random.randint(0,580),random.randint(0,580))]
                  self.snak_len = 1
                  return True

          return False
