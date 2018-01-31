#!/usr/bin/python
import pyganim
import os
import sys
import random
import pygame


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

earthAnim = pyganim.PygAnimation([('sprite/earth-sprite/planet-earth_000000.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000001.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000002.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000003.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000004.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000005.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000006.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000007.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000008.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000009.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000010.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000011.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000012.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000013.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000014.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000015.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000016.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000017.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000018.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000019.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000020.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000021.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000022.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000023.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000024.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000025.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000026.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000027.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000028.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000029.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000030.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000031.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000032.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000033.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000034.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000035.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000036.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000037.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000038.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000039.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000040.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000041.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000042.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000043.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000044.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000045.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000046.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000047.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000048.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000049.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000050.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000051.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000052.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000053.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000054.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000055.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000056.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000057.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000058.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000059.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000060.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000061.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000062.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000063.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000064.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000065.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000066.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000067.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000068.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000069.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000070.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000071.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000072.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000073.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000074.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000075.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000076.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000077.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000078.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000079.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000080.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000081.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000082.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000083.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000084.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000085.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000086.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000087.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000088.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000089.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000090.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000091.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000092.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000093.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000094.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000095.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000096.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000097.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000098.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000099.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000100.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000101.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000102.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000103.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000104.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000105.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000106.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000107.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000108.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000109.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000110.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000111.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000112.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000113.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000114.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000115.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000116.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000117.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000118.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000119.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000120.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000121.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000122.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000123.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000124.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000125.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000126.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000127.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000128.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000129.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000130.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000131.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000132.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000133.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000134.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000135.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000136.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000137.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000138.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000139.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000140.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000141.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000142.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000143.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000144.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000145.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000146.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000147.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000148.png' , 20),
                                  ('sprite/earth-sprite/planet-earth_000149.png' , 20),
])
                                  
earthAnim.play()

gameDisplay = pygame.display.set_mode((display_width, display_height ))
pygame.display.set_caption('Fur Shmup')
clock = pygame.time.Clock()

#main functions



titlePic = pygame.image.load("images/title.png")
backGroundPic = pygame.image.load("images/bg.png")



pygame.mixer.music.load("music/silent_col.ogg")
pygame.mixer.music.play()


#play background sprite



#load title image

def title(x,y):
	gameDisplay.blit(backGroundPic , (0,0))
	earthAnim.blit(gameDisplay, (1400,700))
	gameDisplay.blit(titlePic, (x,y,))
	



x = (display_width * 0)
y = (display_height * 0)

#terminal/cmd/cli text


#if crash, then close python and pygame processes.


crashed = False

while not crashed:

	for event in pygame.event.get() :
		if event.type == pygame.QUIT:
			crashed = True
			
	title(500,100)
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()
