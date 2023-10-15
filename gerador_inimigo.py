import pygame
from inimigos import Enemy, enemies_list
import random

random.seed(None, 2)

def generateEnemy():
    num = len(enemies_list)
    r = random.randrange(num)
    e = Enemy(r, 1)
    return e