import pygame
import numpy as np
import time

from Snak import Snak
from Food import Food
from Breading_Room import Breading_Room
from Full_Snake import Full_Snake

WIDTH = 600.000
HEIGHT =600.000

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
SIZE = 20
FRAME_RATE = 0.050

def sigmoid(x):
    return 1 / (1 + np.e ** -x)

class Win:
    def __init__(self, snak_len, no_of_snaks):
        pygame.init()
        self.window = pygame.display.set_mode((int(WIDTH),int(HEIGHT)))
        pygame.display.set_caption('Sapoolaaa')
        self.clock = pygame.time.Clock()
        self.window.fill(WHITE)
        pygame.display.flip()
        self.run = True
        #Snake
        #self.snake_body = [Snak(0,300)]
        #self.snak_len = 1
        print("ARgv:",snak_len,no_of_snaks)

        self.LIFE = 60 #10K Steps


        self.SPEED_X =1
        self.SPEED_Y =0
        self.total_Snaks = int(no_of_snaks)
        self.snaks_array = []
        self.snak_len = int(snak_len)

        self.Genration = 1
        self.total_Alive = self.total_Snaks
        self.Breading_Room = Breading_Room(self.snak_len)

        self.initilize_Snaks(self.snak_len)
        self.food = self.new_Food()
        self.start()


    def initilize_Snaks(self, snak_len):
         for i in xrange(0,self.total_Snaks):
             self.snaks_array.append(Full_Snake(snak_len))
             self.snaks_array[i].initiaze_network()
             #self.foods_array.append(Food())

    def create_new_Genreation(self):
            self.snaks_array = self.Breading_Room.make_love(self.snaks_array)
            self.Genration += 1
            self.LIFE = 0
            self.total_Alive = len(self.snaks_array)
            self.total_Snaks = len(self.snaks_array)
            print("New Genration #",self.Genration, " new BreadLenght:",len(self.snaks_array))



    def new_Food(self):
        food = Food();
        return food

    def get_input(self):
         # self.SPEED_X
         # self.SPEED_Y
         #
         # key = 0
         # stuck=True
         # while stuck:
         #
         #      for event in pygame.event.get():
         #          if event.type == pygame.KEYDOWN:
         #              if event.key = pygame.K_DOWN:
         #                  if stuck:
         #                      stuck = False
         #                  else
         #                      stuck = True


              # if event.type == pygame.QUIT:
              #     self.run = False
              #
              # elif event.type == pygame.KEYDOWN:
              #     self.SPEED_X = 0
              #     self.SPEED_Y = 0
              #     if event.key == pygame.K_UP:
              #         self.SPEED_Y = -1
              #     elif event.key == pygame.K_DOWN:
              #         self.SPEED_Y = 1
              #     elif event.key == pygame.K_RIGHT:
              #         self.SPEED_X = 1
              #     elif event.key == pygame.K_LEFT:
              #         self.SPEED_X = -1
              #     elif event.key == pygame.K_s:
              #         self.grow()

         for i in xrange(0,self.total_Snaks):
                x_Snake = self.snaks_array[i]

                if x_Snake.isAlive:
                    # dis_left = x_Snake.dis_up
                    # dis_ahead = x_Snake.dis_right
                    # dis_right = x_Snake.dis_down

                    #arange obstical dis in Fview acording to diractionof mouvment

                    #Right
                    if x_Snake.SPEED_X == 1 and x_Snake.SPEED_Y == 0:
                        dis_left = x_Snake.dis_up
                        dis_ahead = x_Snake.dis_right
                        dis_right = x_Snake.dis_down

                    # LEft
                    elif x_Snake.SPEED_X == -1 and x_Snake.SPEED_Y == 0:
                        dis_left = x_Snake.dis_down
                        dis_ahead = x_Snake.dis_left
                        dis_right = x_Snake.dis_up

                    # Down
                    elif x_Snake.SPEED_Y == 1 and x_Snake.SPEED_X == 0:
                        dis_left = x_Snake.dis_right
                        dis_ahead = x_Snake.dis_down
                        dis_right = x_Snake.dis_left
                    # Up
                    elif x_Snake.SPEED_Y == -1 and x_Snake.SPEED_X == 0:
                        dis_left = x_Snake.dis_left
                        dis_ahead = x_Snake.dis_up
                        dis_right = x_Snake.dis_right


                    input_vector = np.array([ dis_left, x_Snake.dis_x_food, dis_ahead, x_Snake.dis_y_food, dis_right ])
                    input_vector = np.array(input_vector, ndmin=2 ).T
                    # print("Input Vecor::",input_vector)
                    x_Snake.get_nxt_move(input_vector)

                    # x_Snake.SPEED_X = self.SPEED_X
                    # x_Snake.SPEED_Y = self.SPEED_Y

                    #print("X_SPEED: ",self.SPEED_X, "Y_SPEED: ",self.SPEED_Y)


    def update_pos(self):
           for s in xrange(0,self.total_Snaks):     ## To update all snaks pos
                x_Snake =  self.snaks_array[s]  ## get individual snake
                if x_Snake.isAlive:
                   x_Snake.update_pos()


    def eat_food(self):
        for i in xrange(0,self.total_Snaks):
              x_Snak = self.snaks_array[i]
              if x_Snak.isAlive:
                  dis = np.sqrt(np.power((x_Snak.snake_body[0].x - self.food.x),2) + np.power((x_Snak.snake_body[0].y - self.food.y),2))
                  # noramalizeing the food distance in range of 0 to 1
                  self.snaks_array[i].dis_food = dis/np.sqrt(np.power(WIDTH,2)+np.power(HEIGHT,2))
                  self.snaks_array[i].dis_x_food = ((x_Snak.snake_body[0].x - self.food.x)/WIDTH)
                  self.snaks_array[i].dis_y_food = ((x_Snak.snake_body[0].y - self.food.y)/HEIGHT)

                  if dis < 1:
                     self.food = self.new_Food()
                     newSnak = Snak(x_Snak.snake_body[x_Snak.snak_len-1].x-(x_Snak.SPEED_X*SIZE), x_Snak.snake_body[x_Snak.snak_len-1].y-(x_Snak.SPEED_Y*SIZE))
                     x_Snak.snake_body.append(newSnak)
                     x_Snak.snak_len = x_Snak.snak_len+1
                     self.snaks_array[i].fitness += 5
                     # print("Yummmm",x_Snak.snak_len)
                     break

    def grow(self):
           x_Snak = self.snaks_array[1]
           self.food = self.new_Food()
           newSnak = Snak(x_Snak.snake_body[x_Snak.snak_len-1].x-(x_Snak.SPEED_X*SIZE), x_Snak.snake_body[x_Snak.snak_len-1].y-(x_Snak.SPEED_Y*SIZE))
           x_Snak.snake_body.append(newSnak)
           x_Snak.snak_len = x_Snak.snak_len+1
           print("Groww",x_Snak.snak_len)



    def bite(self):
        for i in xrange(0,self.total_Snaks):
            x_Snake = self.snaks_array[i]
            if x_Snake.snak_len > 1 and x_Snake.isAlive:
               if x_Snake.bite():
                    # print('Die by bite')
                    self.snaks_array[i].isAlive = False
                    self.total_Alive -= 1
                    if self.total_Alive ==0:
                        self.create_new_Genreation()
                        return
               else:
                   self.snaks_array[i].fitness += 0.001
            # print('\n',x_Snake.snake_body[0].x,',',x_Snake.snake_body[0].y)
            # print('\n',WIDTH,',',HEIGHT)

            # Die when hit the wall
            # if self.snaks_array[i].isAlive and x_Snake.snake_body[0].x > WIDTH or x_Snake.snake_body[0].x < 0 or x_Snake.snake_body[0].y > HEIGHT or x_Snake.snake_body[0].y <0:
            #     #die
            #     # print('Dia by wall')
            #     self.snaks_array[i].isAlive = False
            #     self.total_Alive -=1
            #     if self.total_Alive ==0:
            #         self.create_new_Genreation()
            #         return


        #self.snaks_array = x_array
        #self.total_Snaks = len(self.snaks_array)




    def draw_Food(self):
         pygame.draw.rect(self.window,BLACK,self.food.at())
         #print('food ',self.food.at())



    def draw_Sake(self):

        for s in xrange(0,self.total_Snaks):         #draw all snaks
            x_Snake = self.snaks_array[s]  # get individual snake
            if (x_Snake.isAlive):
                 for snak in x_Snake.snake_body:   # draw individual snake
                     pygame.draw.rect(self.window, x_Snake.s_Color ,snak.at())

    def draw_score(self):
        font = pygame.font.SysFont(None,20)
        S0_Fitness = font.render('Fitness one:'+str(self.snaks_array[0].fitness),True,(255,255,255),(0,0,0,0))
        # S1_Fitness = font.render('Fitness two:'+str(self.snaks_array[1].fitness),True,(255,255,255),(0,0,0,0))
        # S2_Fitness = font.render('Fitness three:'+str(self.snaks_array[2].fitness),True,(255,255,255),(0,0,0,0))
        Genration  = font.render('Genration:'+str(self.Genration),True,(255,255,255),(0,0,0,0))
        total_Alive = font.render('total Alive:'+str(self.total_Alive),True,(255,255,255),(0,0,0,0))
        life = font.render('Life remain:'+str(self.LIFE),True,(255,255,255),(0,0,0,0))
        self.window.blit(S0_Fitness,[110,10,100,60])
        # self.window.blit(S1_Fitness,[220,10,100,60])
        # self.window.blit(S2_Fitness,[330,10,100,60])
        self.window.blit(Genration,[10,10,100,60])
        self.window.blit(total_Alive,[10,60,100,60])
        self.window.blit(life,[10,100,100,60])



    def start(self):
        while self.run:
           time.sleep(FRAME_RATE)
           self.window.fill(WHITE)
           self.get_input()
           self.update_pos()
           self.eat_food()
           self.bite()
           self.draw_Food()
           self.draw_Sake()
           self.draw_score()
           pygame.display.flip()
           #self.clock.tick(FRAME_RATE)
           self.LIFE += 1;

           # if self.LIFE == 0:
               # self.create_new_Genreation()
