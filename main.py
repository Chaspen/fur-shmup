import pygame
from pygame.locals import *
from pygame import mixer
import pyganim
from pysndfx import AudioEffectsChain
import sys

#init everything
pygame.mixer.pre_init(frequency=44100, size=-16, channels=10, buffer=4096)
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

def InitMain():
	
    #display resolutions
    display_width =  1500
    display_height = 800
    #color definition
    black = (0,0,0)
    white = (256,256,256)
    red = (255,0,0)
    #general game setup
    gameDisplay = pygame.display.set_mode((display_width, display_height ))
    pygame.display.set_caption('FuzzForce')
    clock = pygame.time.Clock()
    #init AudioEffectsChain
    MenuFX = (
        AudioEffectsChain()
	    .reverb()
    )
    #load media and play
    titlePic = pygame.image.load('images/title.png')
    backGroundPic = pygame.image.load('images/bg.png')
    pygame.mixer.music.load('music/silent_col.ogg')
    pygame.mixer.music.play()

    def QuitAct():
        pygame.quit()
        quit()

    def title(x,y):                                              #title graphics
	    gameDisplay.blit(backGroundPic , (0,0))
	    gameDisplay.blit(titlePic, (x,y,))

    ConfirmStart = pygame.mixer.Sound('sfx/start-confirm.wav')

    x = (display_width * 0)
    y = (display_height * 0)

    #make images scalable
    GetBGSize = backGroundPic.get_rect()
    GetLogoSize = titlePic.get_rect()


    crashed = False
    while not crashed:                                            #Game loop starts here.
	    for event in pygame.event.get() :
		    if event.type == pygame.QUIT:
			    crashed = True                               #if crash, then close python and pygame processes.
	    if event.type == pygame.locals.KEYDOWN:                    #key registers start here
		    if event.key == pygame.K_SPACE:                        #when press space, stop (almost) everything and do the next thing
			    pygame.mixer.music.fadeout(3)
			    ConfirmStart.play(0)
			    titlePic.set_alpha(0)
		    if event.key == pygame.K_ESCAPE:
			    quit()
			    pygame.quit()


	    title(450,50)
	    pygame.display.update()
	    clock.tick(60)
    QuitAct()
