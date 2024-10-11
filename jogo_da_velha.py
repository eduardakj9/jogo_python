# Example file showing a basic pygame "game loop"
import pygame #importa a bibliotea pygame para o script

# pygame configuraçao
pygame.init() #inicializaçao do pygame
screen = pygame.display.set_mode((500,500)) #definiçao do tamanho de tela 
pygame.display.set_caption ('jogo da velha') #nome da janela do jogo
clock = pygame.time.Clock()#biblioteca de tempo

fonte_quadrinhos = pygame.font,Sysfont('comic sans ms,30') #importar fonte
running = True #variavel controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', true, "red")
personagem_y = fonte_quadrinhos.render ('O' , true, "red ")
cor_fundo = 1 #azul
cor_fundo = 2 #vermelho
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           print('clicou')
           cor_fundo = = cor_fundo + 1
        if (cor_fundo > 3):
            cor_fundo = 1

   
    if cor_fundo == 1:
         screen.fill ('black')  
         screen.blit ('personagem_x,(250,250))
    elif cor_fundo ==2:
        screen.fill (black)
        screen.blit (personagem_y,(250,250))
    else: 
         screen.fill('purple')


#flip() o display para atualizar a pagina
pygame.disolay.flip()
clock.tick(60)  # limita o fps para 60

pygame>quit()