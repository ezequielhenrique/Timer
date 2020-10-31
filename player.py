import pygame


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('sound/alert.wav')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
