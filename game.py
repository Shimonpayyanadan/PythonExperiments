import pygame
import random
import time

class Players:
    name = ""
    health = 0
    skill = 0

    def __init__(self,plyname,plyskill):
        self.health = 100
        self.name = plyname
        self.skill = plyskill

        print("\n\tWelcome to the game", self.name,"\n")
        print("\tThe skill point for your skill is:", self.skill,"\n")

    # Drawing the players
    def player1_gx(screen, x, y):
        # head
        pygame.draw.ellipse(screen, RED, [1 + x, y, 10, 10], 0)

        # legs
        pygame.draw.line(screen, RED, [5 + x, 17 + y], [10 + x, 27 + y], 2)
        pygame.draw.line(screen, RED, [5 + x, 17 + y], [x, 27 + y], 2)

        # body
        pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

        # arms
        pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
        pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)




class Enemies:
    ename = ""
    ehealth = 0
    eskill = 0
    enamelist = ["Ultron", "Megabot", "FireMonster", "EvilGenie", "Predator","Demon","Casper"]

    def __init__(self):
        self.ename = random.choice(self.enamelist)
        self.eskill = random.randrange(10, 60, 9)
        self.ehealth = 60

        print("\n\t\t",self.ename,"\t","Damage Point: ",self.eskill)



def enemyinit():

    print("\n\n\tSetting up your enemies...")
    time.sleep(2)
    print("\n\n\tYour enemies are ready!")
    print("\n\tCheck out your enemies:")
    e1 = Enemies()
    e2 = Enemies()
    e3 = Enemies()
    e4 = Enemies()
    e5 = Enemies()





def playerinit():


    print("\tPlease fill in your details\n")
    plynum=int(input("\tEnter the number of players (Max. 2) :"))
    if plynum==1:
        plyname=input("\tEnter your name:")
        p1 = Players(plyname,plyskill=30)

    elif plynum == 2:
        plyname = input("\tEnter Player 1 name :")
        p1 = Players(plyname, plyskill=25)
        plyname = input("\tEnter Player 2 name :")
        p2 = Players(plyname, plyskill=25)

#Drawing the players
def player1_gx(screen, x, y):
    #head
    pygame.draw.ellipse(screen, RED, [1 + x, y, 10, 10], 0)

    #legs
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [x, 27 + y], 2)

    #body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    #arms
    pygame.draw.line(screen,RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

def player2_gx(screen, x2, y2):
    #head
    pygame.draw.ellipse(screen, BLUE, [1 + x2, y2, 10, 10], 0)

    #legs
    pygame.draw.line(screen, BLUE, [5 + x2, 17 + y2], [10 + x2, 27 + y2], 2)
    pygame.draw.line(screen, BLUE, [5 + x2, 17 + y2], [x2, 27 + y2], 2)

    #body
    pygame.draw.line(screen, BLUE, [5 + x2, 17 + y2], [5 + x2, 7 + y2], 2)

    #arms
    pygame.draw.line(screen, BLUE, [5 + x2, 7 + y2], [9 + x2, 17 + y2], 2)
    pygame.draw.line(screen, BLUE, [5 + x2, 7 + y2], [1 + x2, 17 + y2], 2)

def enemy_gx(screen,ex,ey):
    pygame.draw.ellipse(screen, BLACK, [1 + ex, ey, 10, 10], 0)



def game():

    playerinit()
    enemyinit()

    print("\n\n\t\tThe game is about to begin...!")




#game()

#Code for window operations
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size=(1000,700)

clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Monster Hunt")

#flag to quit
stop=0
#initializing players cordinate position
x=10
y=10

x2=10
y2=80

#initalizing players velocities
xv=0
yv=0

xv2=0
yv2=0

#initalizing enemy coordinates

ex=random.randrange(10,900,5)
ey=random.randrange(10,650,5)

exv=3
eyv=3

#Loop for the entire window operations
while stop==0:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            stop=1

            #For player 1
#       on pressing an arrow key
        # xv, yv = velocity at which the object moves
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                xv = -3
            elif event.key == pygame.K_RIGHT:
                xv = 3
            elif event.key == pygame.K_UP:
                yv = -3
            elif event.key == pygame.K_DOWN:
                yv = 3
                #         on releasing an arrow key
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xv = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yv = 0

        #For player 2
        if event.type==pygame.QUIT:
            stop=1
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                xv2 = -3
            elif event.key == pygame.K_d:
                xv2 = 3
            elif event.key == pygame.K_w:
                yv2 = -3
            elif event.key == pygame.K_s:
                yv2 = 3
                    #         on releasing an arrow key
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a or event.key == pygame.K_d:
                xv2 = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                yv2 = 0


    #updating the player coordinates
    x=x+xv
    y=y+yv

    x2=x2+xv2
    y2=y2+yv2

    #updating enemy coordinates
    if ex>950 or ex<10:
        exv=exv*-1
    if ey>650 or ey<10:
        eyv=eyv*-1

    ex=ex+exv
    ey=ey+eyv




    screen.fill(WHITE)
    player1_gx(screen,x,y)
    player2_gx(screen,x2,y2)
    enemy_gx(screen,ex,ey)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


