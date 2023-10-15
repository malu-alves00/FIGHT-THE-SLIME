import pygame
import numpy
import pandas 

pygame.init()
screenSize = [900,1000]
screen = pygame.display.set_mode(screenSize)
prev_pos = (0,0)
array_pos = []
array_final = []
writeToArray = False
header_list = ['shape_number','point','x','y']
i = 0
j = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            writeToArray = True
            prev_time = pygame.time.get_ticks()
            prev_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            writeToArray = False
            data_frame = pandas.DataFrame(array_pos)
            data_frame.to_csv('arrays_test.csv', index = False, header = header_list)
            j += 1
        if event.type == pygame.MOUSEMOTION:
            pos=event.pos
    
    if(writeToArray):
        array_pos.append([j, i, pos[0],pos[1]])
        i += 1
        print(array_pos)

    screen.fill((89, 85, 115))
    pygame.display.flip()