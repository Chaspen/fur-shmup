import pygame
from pygame.locals import *
from pygame import mixer
import pyganim
from pysndfx import AudioEffectsChain

#init everything
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
#display resolutions
display_width =  1500
display_height = 800
#color definition
black = (0,0,0)
white = (256,256,256)
red = (255,0,0)
#general game setup
gameDisplay = pygame.display.set_mode((display_width, display_height ))
pygame.display.set_caption('Fur Shmup')
clock = pygame.time.Clock()
#init AudioEffectsChain
MenuFX = (
    AudioEffectsChain()
	.reverb()
)
#load media and play
titlePic = pygame.image.load('images/title.png')
backGroundPic = pygame.image.load('images/bg.png')
pygame.mixer.music.load('music/menu-music.ogg')
pygame.mixer.music.play()

def title(x,y): #title graphics
	gameDisplay.blit(backGroundPic , (0,0))
	gameDisplay.blit(titlePic, (x,y,))

ConfirmStart = pygame.mixer.Sound('sfx/start-confirm.wav')

x = (display_width * 0)
y = (display_height * 0)

crashed = False
while not crashed:      #Game loop starts here.
	for event in pygame.event.get() :
		if event.type == pygame.QUIT:
			crashed = True#if crash, then close python and pygame processes.
	if event.type == pygame.locals.KEYDOWN: #key registers start here
		if event.key == pygame.K_SPACE: #when press space, stop (almost) everything and do the next thing
			pygame.mixer.music.stop()
			ConfirmStart.play(0)
			pygame.mixer.stop()
			titlePic.set_alpha(0)
		else:
			pygame.mixer.stop()
		if event.key == pygame.K_ESCAPE:
			quit()
			pygame.quit()


	title(450,50)
	pygame.display.update()
	clock.tick(60)
#Game loop ends here
pygame.quit()
quit()
