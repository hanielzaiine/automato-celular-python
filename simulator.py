import random
import time

import pygame

from game import game_of_life

# plano vazio
SEED = [[0 for _ in range(50)] for _ in range(50)]

# Flag para alterar status de n celulas
x_axis = int(input("Entre com a cordenada X: "))
y_axis = int(input("Entre com a cordenada Y: "))

while x_axis < 50 and y_axis < 50:

    SEED[x_axis][y_axis] = 1
    x_axis = int(input("Entre com a cordenada X: "))
    y_axis = int(input("Entre com a cordenada Y: "))

pygame.init()

screen = pygame.display.set_mode((550, 550))


def draw_matrix(matrix):
    '''
    Função para desenhar o plano
    '''

    # preenche a tela de preto
    screen.fill([0, 0, 0])

    # percorre o plano desenhando as células com seus valores
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell:
                # caso a célula esteja viva, a pinte de branco
                pygame.draw.rect(screen, (255, 255, 255),
                                 (11*c, 11*r, 10, 10))


# define a seed como um dos valores de exemplo do começo
seed = SEED

# desenha o estado inicial de nossa seed
draw_matrix(seed)

pygame.display.flip()

time.sleep(1)

while True:
    # PROCESSAMENTO DE ENTRADA
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        break

    # ATUALIZAÇÃO DO JOGO
    seed = game_of_life(seed)

    # DESENHO
    draw_matrix(seed)
    pygame.display.flip()

    time.sleep(0.30)
