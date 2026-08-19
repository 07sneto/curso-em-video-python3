# pygame é a biblioteca para criação de jogos.
    # isso é, criar jogos, sons, imagens e animações.

import pygame
pygame.mixer.init()
pygame.mixer.music.load("exe021.mp3")
pygame.mixer.music.play()

# o input é só para o programa continuar aberto, ai a musica irá continuar tocando ate o programar fechar.
input()
