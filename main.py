import pygame
from pygame.locals import *
import pyganim


pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

display_width =  1600
display_height = 900



#color definition
black = (0,0,0)
white = (256,256,256)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width, display_height ))
pygame.display.set_caption('Fur Shmup')
clock = pygame.time.Clock()


#main functions



titlePic = pygame.image.load("images/title.png")
backGroundPic = pygame.image.load("images/bg.png")



pygame.mixer.music.load("music/silent_col.ogg")
pygame.mixer.music.play()




#load title image

def title(x,y):
	gameDisplay.blit(backGroundPic , (0,0))
	gameDisplay.blit(titlePic, (x,y,))


def ConfirmStart():
	pygame.mixer.music.load()


x = (display_width * 0)
y = (display_height * 0)

#if crash, then close python and pygame processes.


crashed = False

while not crashed:



	for event in pygame.event.get() :
		if event.type == pygame.QUIT:
			crashed = True
	if event.type == pygame.locals.KEYDOWN:
		if event.key == pygame.K_SPACE:
			pygame.mixer.music.fadeout(700)

	title(500,100)
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()
