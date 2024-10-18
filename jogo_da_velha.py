# Example file showing a basic pygame "game loop"
import pygame #importa a bibliotea pygame para o script

# pygame configuraçao
pygame.init() #inicializaçao do pygame
screen = pygame.display.set_mode((600,600)) #definiçao do tamanho de tela 
pygame.display.set_caption ('jogo da velha') #nome da janela do jogo
clock = pygame.time.Clock()#biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('comic sans ms',100) #importar fonte
running = True #variavel controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, "red")
personagem_y = fonte_quadrinhos.render ('O' , True, "red ")
cor_fundo = 1 #azul

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           print('clicou')
           cor_fundo = cor_fundo + 1
        if (cor_fundo > 3):
            cor_fundo = 1

    #desenha tabuleiro
    #                                 origem   destino
    #                                 (x . y)   (x.y)
    pygame.draw.line(screen,'white',(200,0), (200,600),  10)
    pygame.draw.line(screen,'white',(400, 0),(400,600), 10)
    pygame.draw.line(screen,'white',(0,200), (600,200), 10)
    pygame.draw.line(screen,'white',(0,400), (600,400), 10)
   
    #                           x  y
    screen.blit(personagem_x,(60,30)) #primeiro
    screen.blit(personagem_y,(260,30)) #segundo
    screen.blit(personagem_y,(460,30)) #terceiro
         

    #flip() o display para atualizar a pagina
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()