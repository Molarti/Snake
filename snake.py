import random
import time
import pygame

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0,0,0)
green = (0,255,0)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake")

game_over = False

x1 = 300
y1 = 400

x1_change = 0
y1_change = 0

clock =pygame.time.Clock()
block =10
b =1
snake_L = []
s = pygame.font.SysFont('comm',25)
def snake_ln(snake_block,list):
    for i in list:
        pygame.draw.rect(dis,black,[i[0],i[1],block,block])

def rez(sc):
    rz = s.render('Счёт:'+ str(sc),True,red)
    dis.blit(rz,[0,0])

food1 = random.randrange(0, 800 - block,block)
food2 = random.randrange(0, 800 - block,block)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1>=800 or x1<0 or y1>=600 or y1<0:
        game_over = True

    x1+=x1_change
    y1+=y1_change
    dis.fill(white)
    #pygame.draw.rect(dis, green,[food1,food2,block,block])

    snake_H = []
    snake_H.append(x1)
    snake_H.append(y1)
    snake_L.append(snake_H)

    if len (snake_L) > b:
        del snake_L[0]

    for i in snake_L[:-1]:
        if i == snake_H:
            game_over = True

    snake_ln(block,snake_L)
    rez(b - 1)
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
    pygame.draw.rect(dis, black, [food1, food2, 10, 10])
    pygame.display.update()


    if x1 == food1 and y1 == food2:
        food1 = random.randrange(0, 800 - block,block)
        food2 = random.randrange(0, 800 - block,block)
        b +=1

    clock.tick(30)

pygame = quit()
quit()