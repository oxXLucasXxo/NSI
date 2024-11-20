import pygame
from pygame.locals import*

class Perso :
    "Définition d'un personnage"
    def __init__(self,nom):
        self.l_sprites={'haut':[pygame.image.load('images/'+nom+'_h'+str(i)+'.png') for i in range(1,10)],
                        'bas': [pygame.image.load('images/'+nom+str(i)+'.png') for i in range(1,10)],
                        'droite' : [pygame.image.load('images/'+nom+'_d'+str(i)+'.png') for i in range(1,9)],
                        'gauche' : [pygame.transform.flip(pygame.image.load('images/'+nom+'_d'+str(i)+'.png'),True,False) for i in range(1,9)]}
        self.direction='bas'
        self.nb_frames=len(self.l_sprites[self.direction])
        self.current_frame=0
        self.x=30
        self.y=30
    def draw(self,screen) :
        self.nb_frames=len(self.l_sprites[self.direction])
        screen.blit(self.l_sprites[self.direction][int(self.current_frame)%self.nb_frames],(self.x,self.y))

pygame.init()

def jeu() :
    screen=pygame.display.set_mode((400,400))
    screen.fill((0,0,0))
    clock=pygame.time.Clock()
    perso=Perso('zelda')
    direction='bas'
    move=False
    stop=False
    while not stop :
        for event in pygame.event.get() :
            if event.type==QUIT :
                pygame.quit()
            elif event.type==KEYDOWN :
                if event.key==K_UP :
                    perso.direction='haut'
                    move=True
                elif event.key==K_DOWN :
                    perso.direction='bas'
                    move=True
                elif event.key==K_RIGHT :
                    perso.direction='droite'
                    move=True
                elif event.key==K_LEFT :
                    perso.direction='gauche'
                    move=True
            elif event.type==KEYUP :
                if event.key==K_UP :
                    perso.current_frame=0
                    perso.direction='haut'
                    move=False
                elif event.key==K_DOWN :
                    perso.current_frame=0
                    perso.direction='bas'
                    move=False
                elif event.key==K_RIGHT :
                    perso.current_frame=0
                    perso.direction='droite'
                    move=False
                elif event.key==K_LEFT :
                    perso.current_frame=0
                    perso.direction='gauche'
                    move=False
        clock.tick(60)
        screen.fill((0,0,0))
        perso.draw(screen)
        pygame.display.flip()
        if move :
            if perso.direction=='gauche' :
                perso.x-=2
            if perso.direction=='droite' :
                perso.x+=2
            if perso.direction=='haut' :
                perso.y-=2
            if perso.direction=='bas' :
                perso.y+=2
            perso.current_frame+=0.08
        else:
            perso.current_frame=0

jeu()
