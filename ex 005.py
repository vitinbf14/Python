import pygame
pygame.init()
pygame.mixer.music.load('tocando mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
