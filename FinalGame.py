import pygame
import random
import time

''' MAKE SURE YOU HAVE pygame module for python3.x '''
#colors used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



class Players(object):

    health=0

    x=10
    y=10

    xv = 0
    yv = 0

    def __init__(self, plyname, plyskill,x,y):
        self.plyname=plyname
        self.plyskill=plyskill
        self.health=300

        self.x=x
        self.y=y

        print("\n\tWelcome to the game", self.plyname,"\n")
        print("\tThe skill point for your skill is:", self.plyskill,"\n")

         #Drawing players
    def player_gx(self,screen,x,y):
        # head
        pygame.draw.ellipse(screen,BLUE , [self.x, self.y, 20, 20], 0)


    def plycord_upd(self,x,y,xv,yv):

        if self.x > 950 or self.x < 10:
            self.xv=self.xv*-1
        if y > 650 or y < 10:
            self.yv=self.yv*-1

        self.x=self.x+self.xv
        self.y=self.y+self.yv

    def damage(self):
        self.health=self.health-10



class Enemies(object):
    ename = ""
    ehealth = 60
    eskill = 0
    enamelist = ["Ultron", "Megabot", "FireMonster", "EvilGenie", "Predator","Demon","Casper"]
    ex=0
    ey=0

    exv = 7
    eyv = 7



    def __init__(self):
        self.ename = random.choice(self.enamelist)
        self.eskill = 20

        self.ex = random.randrange(10, 900, 10)
        self.ey = random.randrange(10, 650, 10)

        print("\n\t\t", self.ename, "\t", "Damage Point: ", self.eskill)

    #Drawing enemies

    def enemy_gx(self,screen,ex, ey):

        BLACK=(0,0,0)
        pygame.draw.ellipse(screen, RED, [self.ex, self.ey, 20, 20], 0)

    def enycord_upd(self,ex,ey,exv,eyv):
        if self.ex > 950 or self.ex < 10:
            self.exv = self.exv * -1
        if ey > 650 or ey < 10:
            self.eyv = self.eyv * -1

        self.ex = self.ex + self.exv
        self.ey = self.ey + self.eyv

def collision(x,y,ex,ey):

    ply_rect = pygame.Rect(x, y, 20, 20)
    eny_rect = pygame.Rect(ex, ey, 20, 20)

    if ply_rect.colliderect(eny_rect):
        return True

#Starting code
print("\t**********************************************")
print("\t\t***********WELCOME*************\n\n")
print("\t\t READ THE INSTRUCTIONS\n")

print("\t Use the arrow keys to control your BLUE player 1\n")

print("\t Use W ,A ,D ,S keys to control your BLUE Player 2\n")

print("\t Try to get NOT HIT by the RED Monsters\n\n")

            #Player initialization
print("\t\tPlease fill in your details\n")
plynum=int(input("\tEnter the number of players (Max. 2) :"))
if plynum==1:
    plyname=input("\tEnter your name:")
    p1 = Players(plyname,plyskill=30,x=10,y=10)

elif plynum == 2:
    plyname = input("\tEnter Player 1 name :")
    p1 = Players(plyname, plyskill=25,x=50,y=50)
    plyname = input("\tEnter Player 2 name :")
    p2 = Players(plyname, plyskill=25,x=700,y=50)


#Enemy Initialization
print("\n\n\tSetting up your enemies...")
time.sleep(2)
print("\n\n\tYour enemies are ready!")
print("\n\tCheck out your enemies:")
e1 = Enemies()
e2 = Enemies()
e3 = Enemies()
e4 = Enemies()
e5 = Enemies()

print("\t\t\t You are all set!")






#Code for window operations
pygame.init()


size=(1000,700)

clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Monster Hunt")

#flag to quit
stop=0
#Loop for the entire window operations
while stop==0:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            stop=1

            # For player 1
            #       on pressing an arrow key
            # xv, yv = velocity at which the object moves
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                p1.xv = -7
            elif event.key == pygame.K_RIGHT:
                p1.xv = 7
            elif event.key == pygame.K_UP:
                p1.yv = -7
            elif event.key == pygame.K_DOWN:
                p1.yv = 7
                #         on releasing an arrow key
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p1.xv = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p1.yv = 0

        # For player 2
    if plynum==2:
        if event.type == pygame.QUIT:
            stop = 1
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                p2.xv = -7
            elif event.key == pygame.K_d:
                p2.xv = 7
            elif event.key == pygame.K_w:
                p2.yv = -7
            elif event.key == pygame.K_s:
                p2.yv = 7
                #         on releasing an arrow key
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a or event.key == pygame.K_d:
                p2.xv = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                p2.yv = 0



     #updating player coordinates
    p1.plycord_upd(p1.x,p1.y,p1.xv,p1.yv)

    if plynum==2:
        p2.plycord_upd(p2.x,p2.y,p2.xv,p2.yv)

    #updating enemy coord
    e1.enycord_upd(e1.ex,e1.ey,e1.exv,e2.eyv)
    e2.enycord_upd(e2.ex,e2.ey,e2.exv,e2.eyv)
    e3.enycord_upd(e3.ex, e3.ey, e3.exv, e3.eyv)
    e4.enycord_upd(e4.ex, e4.ey, e4.exv, e4.eyv)
    e5.enycord_upd(e5.ex, e5.ey, e5.exv, e5.eyv)

    #COLLISION DETECTION

    if collision(p1.x,p1.y,e1.ex,e1.ey) or collision(p1.x,p1.y,e2.ex,e2.ey) or collision(p1.x,p1.y,e3.ex,e3.ey) or collision(p1.x,p1.y,e4.ex,e4.ey) or collision(p1.x,p1.y,e5.ex,e5.ey) :
        p1.health=p1.health-e1.eskill

    if plynum==2:
        if collision(p2.x,p2.y,e1.ex,e1.ey) or collision(p2.x,p2.y,e2.ex,e2.ey) or collision(p2.x,p2.y,e3.ex,e3.ey) or collision(p2.x,p2.y,e4.ex,e4.ey) or collision(p2.x,p2.y,e5.ex,e5.ey) :
            p2.health=p2.health-e2.eskill



    screen.fill(BLACK)


    if p1.health >0:

        p1.player_gx(screen,p1.x,p1.y)

    if plynum==2:
        if p2.health>0:

            p2.player_gx(screen,p2.x,p2.y)

    e1.enemy_gx(screen,e1.ex,e1.ey)
    e2.enemy_gx(screen,e2.ex,e2.ey)
    e3.enemy_gx(screen,e3.ex,e3.ey)
    e4.enemy_gx(screen,e4.ex,e4.ey)
    e5.enemy_gx(screen,e5.ex,e5.ey)

    #Texts to display
    # Font Used
    if p1.health <= 0:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        p1health = font.render("Player 1 Dead ", True, RED)
        screen.blit(p1health, [50, 5])

    else:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        p1health = font.render("Player 1 Health: "+str(p1.health), True, WHITE)
        screen.blit(p1health, [50, 5])

    if plynum==2:
        if p2.health <= 0:
            font = pygame.font.SysFont('Calibri', 25, True, False)
            p2health = font.render("Player 2 Dead" , True, RED)
            screen.blit(p2health, [750, 5])
        else:

            font = pygame.font.SysFont('Calibri', 25, True, False)
            p2health = font.render("Player 2 Health: "+str(p2.health), True, WHITE)
            screen.blit(p2health, [750, 5])

    if plynum==2:
        if p1.health <= 0 and p2.health <= 0 :
            font = pygame.font.SysFont('Calibri', 70, True, False)
            gamestatus = font.render("Game Over ", True, WHITE)
            screen.blit(gamestatus, [350, 350])


    if p1.health <= 0 :
        font = pygame.font.SysFont('Calibri', 70, True, False)
        gamestatus = font.render("Game Over ", True, WHITE)
        screen.blit(gamestatus, [350, 350])



    pygame.display.flip()
    clock.tick(60)

pygame.quit()



