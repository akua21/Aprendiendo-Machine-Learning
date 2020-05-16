import pygame
import numpy as np
import time
import random

# Iniciar pygame
pygame.init()

# Crear pantalla del juego
resolution_screen = (1000, 1000)
screen = pygame.display.set_mode(resolution_screen)

# Poner el fondo como gris oscuro
bg = 25, 25, 25

# Número de celdas en el eje x e y
numCells = (25, 25)

sizeCells = (resolution_screen[0]/numCells[0], resolution_screen[1]/numCells[1])

# Estado del juego. Vivas = 1, muertas = 0
gameState = np.zeros(numCells)

# El palito
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1


# Control de la pausa
pause = False




# Bucle de ejecucion
while True:

    # Copia del juego
    newGameState = np.copy(gameState)

    # Limpiar pantalla
    screen.fill(bg)
    time.sleep(0.1)

    # Registrar interrupcion de teclado
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause

        mouseClick = pygame.mouse.get_pressed()[0]

        if mouseClick == 1:
            posMouse = pygame.mouse.get_pos()
            cellPressed = (int(np.floor(posMouse[0]/sizeCells[0])), int(np.floor(posMouse[1]/sizeCells[1])))
            print(cellPressed)
            newGameState[cellPressed[0], cellPressed[1]] = 1


    # Bucle para recorrer las celdas
    for x in range(0, numCells[0]):
        for y in range(0, numCells[1]):
            if not pause:
                # Vecinos
                n_neigh = gameState[(x-1) % numCells[0], (y-1) % numCells[1]] + \
                          gameState[(x-1) % numCells[0], (y) % numCells[1]]   + \
                          gameState[(x-1) % numCells[0], (y+1) % numCells[1]] + \
                          gameState[(x) % numCells[0],   (y-1) % numCells[1]] + \
                          gameState[(x) % numCells[0],   (y+1) % numCells[1]] + \
                          gameState[(x+1) % numCells[0], (y-1) % numCells[1]] + \
                          gameState[(x+1) % numCells[0], (y) % numCells[1]]   + \
                          gameState[(x+1) % numCells[0], (y+1) % numCells[1]]

                # Reglas

                # Regla 1: Una celda muerta con 3 vecinas vivas "revive"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1


                # Regla 2: Una celda viva con menos de 2 o más de 3 vecinas vivas, "muere"
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # Polígono de cada celda a dibujar
            polygon = [((x)   * sizeCells[0], (y)   * sizeCells[1]),
                       ((x+1) * sizeCells[0], (y)   * sizeCells[1]),
                       ((x+1) * sizeCells[0], (y+1) * sizeCells[1]),
                       ((x)   * sizeCells[0], (y+1) * sizeCells[1])]

            color = (128, 128, 128)
            border = 1

            # Dibujamos la celda para cada par de x e y
            if newGameState[x, y] == 1:
                color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                border = 0

            pygame.draw.polygon(screen, color, polygon, border)

    # Actualizar el estado

    gameState = np.copy(newGameState)

    pygame.display.flip()
