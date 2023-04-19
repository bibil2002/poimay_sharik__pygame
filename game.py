#! /home/bibil2002/anaconda3/bin/python3.10

import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
number_balls = 5
balls =[]
counter = 0 # счетчик очков

def new_ball(x, y, r, delta_x, delta_y, color):
    '''
    добавляет новый круг
    :param x:  координата центра
    :param y: координата центра
    :param r: радиус
    следующие числа заменяют угол напрвления движения
    :param delta_x: изменение координаты x за обновление экрана
    :param delta_y: изменение координаты y за обновление экрана
    :param color: цвет круга
    '''

    global balls

    balls.append({'x':x, 'y': y, 'r':r, 'delta_x':delta_x, 'delta_y':delta_y, 'color':color})

def click(event):
    '''
    Удаляет круги в которые попали и считает очки.
    '''
    global counter
    flag = False # попали ли мы хоть в какой-то круг

    for i in range(len(balls)):


        if ((balls[i]['x'] - event.pos[0])**2 + (balls[i]['y'] - event.pos[1])**2)** 0.5 <= balls[i]['r']:
            balls.pop(i)           # чтобы не было ошибки
            balls.insert(i,0)      # вышли за пределы диапазона списка
            counter += 1
            flag = True

    for i in range(balls.count(0)): # удаляем 0 из списка шаров
        balls.remove(0)

    if flag == False:
        counter -= 1
    print(counter)







def processing_balls():
    '''
    отвечает за движение кругов.И случайным образом изменеят напрвление
    движения когда центр круга выходит за рамки экрана.
    '''





    for i in range(len(balls)):
        balls[i]['x'] += balls[i]['delta_x']
        balls[i]['y'] += balls[i]['delta_y']
        circle(screen, balls[i]['color'], (balls[i]['x'], balls[i]['y']), balls[i]['r'])
        if balls[i]['x'] > 1200:
            balls[i]['delta_x'] = randint(-50, -10)
            balls[i]['delta_y'] = randint(-50, 50)

        elif balls[i]['x'] < 0:
            balls[i]['delta_x'] = randint(10, 50)
            balls[i]['delta_y'] = randint(-50, 50)

        if balls[i]['y'] > 900:
            balls[i]['delta_x'] = randint(-50, 50)
            balls[i]['delta_y'] = randint(-50, 0)
        elif balls[i]['y'] < 0:
            balls[i]['delta_x'] = randint(-50, 50)
            balls[i]['delta_y'] = randint(0, 50)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    processing_balls()


    if len(balls) <= number_balls: # ограничение числа кругов
        new_ball( x = randint(100,700),
                  y = randint(100,500),
                  r = randint(30,50),
                  delta_x = randint(-50,50),
                  delta_y = randint(-50,50),
                  color = COLORS[randint(0, 5)])




    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()