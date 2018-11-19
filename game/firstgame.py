import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

shoot=[pygame.image.load('shoot.png')]
bg = pygame.image.load('bg.png')
r=[pygame.image.load('rect.png')]
gameover = pygame.image.load('gameover.png')
blast=pygame.image.load('blast.png')
blast1=pygame.transform.scale(blast,(58,35))


clock = pygame.time.Clock()

bulletcount=0
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = (self.x, self.y + 11, 50, 110)
        

    def draw(self, win):
        win.blit(shoot[0],(self.x,self.y))
        self.hitbox = (self.x, self.y + 11, 50, 110)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

class projectile(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8 

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
class rectangle(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vel=2
        self.Shot=0
        self.hitbox = (self.x-3, self.y-3, 43, 20)
    def fall(self,win):
        win.blit(r[0],(self.x,self.y))
        self.hitbox = (self.x-3, self.y-3, 43, 20)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)





def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for rect in rectangles:
        rect.fall(win)    
    pygame.display.update()
    
    man.draw(win)

def checkIfLost(listOfRects):
    countFalled = 0
    for rect in listOfRects:
        if rect.y >=500:
            countFalled +=1
    return countFalled

#mainloop
font = pygame.font.SysFont("arial", 30)
text = font.render('Score: ' + str(bulletcount), 1, (255,0,0))
win.blit(text, (200,200))
man = player(200,350, 64,64)
rectangles=[]
bullets = []
run = True
shootLoop=0
count = 0
c=0
while run:
    clock.tick(27)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for rect in rectangles:
        for bullet in bullets:
            if bullet.x>rect.hitbox[0] and bullet.x <rect.hitbox[0]+rect.hitbox[2]:
                if bullet.y< rect.hitbox[1]+rect.hitbox[3] and bullet.y>rect.hitbox[1]:
                    bulletcount+=1
                    rect.Shot+=1
                    if rect.Shot>=3:
                        rectangles.pop(rectangles.index(rect))
                        win.blit(blast1,(rect.x,rect.y))
                        pygame.display.update()
                    else:
                        bullets.pop(bullets.index(bullet))
                        win.blit(blast1,(rect.x,rect.y))
                        pygame.display.update()
    
    for bullet in bullets:
        if bullet.y < 500 and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    position=random.randrange(1,499,50)
    if len(rectangles) is 0:
        rectangles.append(rectangle(position,1))
    for rect in rectangles:
        if rect.y < 500 and rect.y > 0:
            rect.y += rect.vel
        else:
            count += 1
            rectangles.pop(rectangles.index(rect))
        if rect.y > 50 and len(rectangles) < 5:
            rectangles.append(rectangle(position,1))

        
  



    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE] and shootLoop==0:
        if len(bullets) < 6:
            bullets.append(projectile((int(man.x + man.width //2)-8),int(man.y + man.height//2-20), 6, (165,42,42)))
        shootLoop=1 
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
   
            
    redrawGameWindow()

    if count >=12:
        print bulletcount
        win.blit(gameover, (0,0))
        pygame.display.update()
        time.sleep(2)
        break 
pygame.quit()        

