import pygame
pygame.init()
pygame.mixer.music.load('')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass