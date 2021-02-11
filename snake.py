import pygame
import random 
import sys
import pygame
import time

def snake():      
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 000 , 000)
    
    width = 20
    height = 20
    
    margin = 1
    grid = []
   
    lost = None
    v = bool(0)
    constante = None
    previous_snek = []
    coms = [38]
    

    for row in range(30):
        grid.append([])
        for column in range(30):
            grid[row].append(0)  
    pygame.init()
    X = 525
    Y = 545
    window_size = [X,Y]
    screen = pygame.display.set_mode((window_size))
    pygame.display.set_caption("snake")
    font = pygame.font.Font('freesansbold.ttf', 32)
    gameover = font.render('GAME OVER', True ,red, black)
    gameover_rect = gameover.get_rect()
    gameover_rect.center = (X//2 , Y//3)
    font2 = pygame.font.Font('freesansbold.ttf', 18)            
    choice = font2.render('press:(g) to play again      press:(k) to leave',True,white,black)
    choice_rect = choice.get_rect()
    choice_rect.center = (X//2 , 2*Y//3)
    points_font = pygame.font.Font('freesansbold.ttf',11)
    done = False
    tick = 0
    clock = pygame.time.Clock()
    snakeY = random.randint(3,22)
    snakeX = random.randint(3,22)
    snakelength = 1
    grid[snakeY][snakeX] = 1
    snek = [[snakeY,snakeX]]
    while not done:
        previous_i = 0
        while(previous_i < len(previous_snek)):
            grid[(previous_snek[previous_i][0])][(previous_snek[previous_i][1])] = 2
            previous_i += 1
        for event in pygame.event.get():
            if(event.type == pygame.QUIT): 
                done = True
        key_input = pygame.key.get_pressed()
        if (key_input[pygame.K_UP]):
            constante = 0
        elif(key_input[pygame.K_LEFT]):
            constante = 1
        elif(key_input[pygame.K_RIGHT]):
            constante = 2
        elif(key_input[pygame.K_DOWN]):
            constante = 3
        if(constante != None):
            if(coms == [38]):
                coms[0] = constante
            elif(constante != coms[(len(coms) - 1)]):
                coms.append(constante)
        if(tick == 0):
            if(len(coms) > 1):
                coms.remove(coms[0])
            if(snakelength < 8):
                tick = 12
            elif(snakelength < 15):
                tick = 10
            elif(snakelength < 20):
                tick = 8
            elif(snakelength < 25):
                tick = 6
            else:
                tick = 3
            if(coms[0] == 0):
                snakeY -= 1 
            elif(coms[0] == 1):
                snakeX -= 1
            elif(coms[0]  == 2):
                snakeX += 1
            elif(coms[0]  == 3):
                snakeY += 1
            while( v == 0):
                aplY = random.randint(3,22)
                aplX = random.randint(3,22)
                if(grid[aplY][aplX] == 0):
                    grid[aplY][aplX] = 10
                    v = 1
            if(snakeY == aplY and  snakeX == aplX):
                v = 0
                snakelength += 1
            snek.append([snakeY, snakeX])
            while(len(snek) > snakelength):
                snek.remove(snek[0])
            if(constante != None):
                if((grid[snakeY][snakeX] == 2) or (snakeX > 24) or (snakeX < 0) or (snakeY > 24) or (snakeY < 0)):
                    lost = 1
                    done = True
            previous_snek = snek
            points = snakelength - 1
        
            points = ("points: ", str(points))
            points = str(points)
            points = points.split("'")
            points = [points[1] , points[3]]
            points = "".join(points)
            point = points_font.render(str(points), True, white, black)
            points_rec = point.get_rect()
            points_rec.center = (X//2 , Y*3//100)
            i = 0
            while(i < snakelength):
                grid[(snek[i][0])][(snek[i][1])] = 1
                i += 1
            screen.fill(black)
            for row in range(25):
                for column in range(25):
                    color = black
                    if (grid[row][column]) == 1:
                        color = white
                    elif(grid[row][column] == 0 or grid[row][column] == 2):
                        color = black
                    elif(grid[row][column] == 10):
                        color = red
                    pygame.draw.rect(screen,
                                    color,
                                    [(margin + width) * column + margin,
                                    (margin + height) * row + margin,
                                    width,
                                    height])
                    if(grid[row][column] == 2):
                        grid[row][column] = 0
            screen.blit(point , points_rec)
            
            
        else:
            tick -= 1
        clock.tick(30)
        pygame.display.update()
    else:
        pygame.init()
    while(lost == 1):
        screen.fill(black)
        screen.blit(gameover , gameover_rect)
        screen.blit(choice , choice_rect)
        end_points = font2.render(str(points),True,white,black)
        end_points_rec = end_points.get_rect()
        end_points_rec.center = (X//2 , Y//2)
        screen.blit(end_points , end_points_rec)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT): 
                lost == 0
                pygame.quit()
                break
            again = pygame.key.get_pressed()
            if(again[pygame.K_g]):
                lost = 0
                snake()
            elif(again[pygame.K_k]):
                lost = 0
        pygame.display.update()
    pygame.quit()

snake()