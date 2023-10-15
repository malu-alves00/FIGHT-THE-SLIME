import pygame
import serial
import datetime
from inimigos import Enemy
from player import Player
from gerador_inimigo import generateEnemy

# Comunicação serial
ser = serial.Serial("COM3",9600)

# Configuração do PyGame e fontes
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('bahnschrift', 30)
clock = pygame.time.Clock()

# Definições
    ## Exibição
screenSize = [1200,800]
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)

    ## Seus poderes, em uma classe herdada porque eu quero e ponto final!! (mentira é porque quero aprender a usar)
class Powers(Player):
    def __init__(self, level):
        Player.__init__(self, level)

    def getPunchDamage(self):
        return (self.level * 50)
    
    def getHealAmount(self):
        return (self.level * 10)

    def getFireDamage(self):
        return (self.level * 5)
    
botao_interface_player = pygame.image.load("imagens/interface/botao_interface_player.png")
status_fundo = pygame.image.load("imagens/interface/status_player.png")
status_fundo = pygame.transform.scale(status_fundo,(601,800))

player = Player(1)
player_name = font.render(player.getName(), False, (255,255,255))

vida_player = font.render("Vida", False, (255,255,255))
mana_player = font.render("Mana", False, (255,255,255))

powers = Powers(1)
curr_enemy = generateEnemy()

DAMAGEPLAYER = pygame.USEREVENT + 1
pygame.time.set_timer(DAMAGEPLAYER, 1000)

if len(player.getInventory()) == 0:
    texto_inv = []
else:
    texto_inv = getTextoInv(player.getInventory())

def getTextoInv(inv):
    a = []
    for item in inv:
        a.extend([[item[0],item[1][2]]])
    print(a)
    return a

def killHandler(curr_enemy, player):
    loot_table = curr_enemy.getLootTable()
    if len(loot_table) > 0:
        inv = player.getInventory()
        player.addInventory(curr_enemy.getLootTable())
    player.addExperience(curr_enemy.getExperienceAwarded())
    del curr_enemy
    curr_enemy = generateEnemy()
    return curr_enemy
    

running = True
while running:
    # O Grande Observador dos Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == DAMAGEPLAYER:
            player.takeDamage(2)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            btn_interface_rect = botao_interface_player.get_rect(topleft = (810,10))
            if btn_interface_rect.collidepoint(event.pos):
                pass

    # Ler linha da porta serial selecionada
    cc=int(ser.readline())
    if cc > 50: # aviso: calibrar pra não poder socar mais de uma vez só
        curr_enemy.takeDamage(powers.getPunchDamage())

    if curr_enemy.getLife() <= 0:
        curr_enemy = killHandler(curr_enemy,player)
        texto_inv = getTextoInv(player.getInventory())
        #print(texto_inv)

    screen.fill((89, 85, 115))
    curr_enemy.showEnemy(50, 100, screen)
    curr_enemy_name = font.render(curr_enemy.getName(), False, (255,255,255))

    screen.blit(status_fundo, (600,0))

    # Barra de status do inimigo
    screen.blit(curr_enemy_name, (50, 680))
    pygame.draw.rect(screen, (128, 255, 132), (50,620, curr_enemy.getLifePercentage()*4,30))

    # Barra de status do player
    #screen.blit(player_name, (700, 80))
    screen.blit(vida_player, (700, 60))
    pygame.draw.rect(screen, (128, 255, 132), (700, 90, player.getLifePercentage()*4,30))

    screen.blit(mana_player, (700, 150))
    pygame.draw.rect(screen, (0, 128, 255), (700, 180, 400, 30))

    pygame.display.flip()

pygame.quit()