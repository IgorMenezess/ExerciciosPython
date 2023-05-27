#Tocar um mp3
import pygame
pygame.init()
pygame.mixer.music.load('terraria.mp3')
pygame.mixer.music.play(-1)
input()
pygame.event.wait()

print ('Tocando...')




