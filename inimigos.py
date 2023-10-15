import pygame
from itens import items, weapons, consumables
import random

random.seed(None, 2)

enemies_list = {
    # enemy_id: [numberid, 'name','life modifier','exp modifier','image location', [[chance,max amount,loot],[chance,max amount,loot]]]
    0:[0, "Slime Verde", 100, 5, "imagens/slime1.png", [[0.8, 2, items[0]]]],
    1:[1, "Blorg e Jr.", 105, 6, "imagens/blorg.png", [[0.8, 2, items[1]]]],
    2:[2, "Lagarto Fantasma", 90, 6, "imagens/lagartofantasma.png", [[0.8, 1, consumables[0]]]],
    3:[3, "Bimfas", 97, 7, "imagens/bimfas.png", [[0.8, 1, weapons[0]]]]
}

class Enemy:
    def __init__(self,enemy_id,level):
        self.enemy = enemies_list[enemy_id]
        self.level = level
        self.name = self.enemy[1]
        self.total_life = level * self.enemy[2]
        self.life = self.total_life
        self.exp_value = level * self.enemy[3]
        self.image = pygame.image.load(self.enemy[4])
        self.killed = False
        self.loot_table = self.createLootTable(self.enemy[5])
        self.image = pygame.transform.scale(self.image, (400,400))
        #print(self.loot_table)
    
    def createLootTable(self, loot_list): # depois, implementar a probabilidade de vir loot
        n = loot_list[0][1]
        amount = random.randrange(n)
        return [[amount, element[2]] for element in loot_list if amount > 0]
        #return [[lootAmount(loot_list) for i in range(len(element))] for element in loot_list if]
    
    def killed(self):
        return [exp_value, loot_table]

    def __del__(self):
      pass

    def showEnemy(self,x,y,screen):
        screen.blit(self.image, (x, y))

    def takeDamage(self,damage):
        self.life -=damage
    
    def getLootTable(self):
        return self.loot_table

    def getLevel(self):
        return self.level

    def getLife(self):
        return self.life

    def getTotalLife(self):
        return self.total_life

    def getLifePercentage(self):
        return (self.life/self.total_life) * 100
    
    def getName(self):
        return self.name

    def getExperienceAwarded(self):
        return self.exp_value