class Player:
    def __init__(self, level):
        self.level = 1
        self.total_life = level * 50
        self.life = self.total_life
        self.name = "Player"
        self.kills = 0
        self.experience = 0
        self.inventory = []
    
    def levelUp(self):
        self.level += 1

    def takeDamage(self, damage):
        self.life -= damage

    def addInventory(self, items):
        for inv_element in self.inventory:
            for item_element in items:
                if inv_element[1][0] == item_element[1][0]:
                    inv_element[0] += item_element[0]
                    items.remove(item_element)
        self.inventory.extend(items)
        
    # Lista dos set
    def addExperience(self, exp):
        self.experience += exp
        if self.experience >= self.level * 5:
            self.levelUp()

    def addKill(self,num):
        self.kills += num

    # Lista dos get
    def getLevel(self):
        return self.level

    def getLife(self):
        return self.life
    
    def getLifePercentage(self):
        return (self.life/self.total_life) * 100

    def getName(self):
        return self.name

    def getInventory(self):
        return self.inventory