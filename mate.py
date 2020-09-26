import pygame
import math
import time
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

front_surface = pygame.surface.Surface((400, 300), pygame.SRCALPHA)
back_surface = pygame.surface.Surface((400, 300), pygame.SRCALPHA)
extra_surface = pygame.surface.Surface((400,300), pygame.SRCALPHA)
line1 = [0, 0, 0, 0]
line2 = [0, 0, 0, 0]

radius1 = 40
radius2 = 20
angle1 = 0
angle2 = 0

line1[0] = 200
line1[1] = 150

time2 = 0.0
time1 = 0.0
ticks = 0
prev_line = [0, 0, 0, 0]
while not done:
        
        while time2 < 3.14:
            time2 += ticks*400/100
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
            while time1 < 3.14:
                
                time1 += ticks*900/100
                line1[2] = int(math.cos(time2)*radius1 + line1[0])
                line1[3] = int(math.sin(time2)*radius1 + line1[1])
                line2[0] = line1[2]
                line2[1] = line1[3]
                line2[2] = int(math.cos(time1)*radius2 + line1[2])
                line2[3] = int(math.sin(time1)*radius2 + line1[3])
                front_surface.set_at((line2[2], line2[3]), (255,0,0))
                pygame.draw.line(back_surface, (255, 255, 255),(line1[0], line1[1]), (line1[2], line1[3]), 2)
                pygame.draw.line(extra_surface, (255, 0, 255),(line2[0], line2[1]), (line2[2], line2[3]), 2)

            
                ticks = time.time()
                pygame.display.flip()
                
                
                screen.blit(back_surface,[0,0])
                screen.blit(front_surface,[0,0])
                screen.blit(extra_surface,[0,0])
                
                prev_line[0] = line1[0]
                prev_line[1] = line1[1]
                prev_line[2] = line1[2]
                prev_line[3] = line1[3]

                back_surface.fill((0,0,0))
                extra_surface.fill(0)
                
                
        
            time1 = 0
        time2 = 0
        