#arecord --device=hw:3,0 --format S16_LE --rate 44100 -c1 test.wav
import pygame
pygame.mixer.init()

pygame.mixer.music.load("test.wav")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	continue