import pygame, sys
from simulation import Simulation
from menu import show_menu

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FPS = 12
GREY = (20, 20 ,20)
CELL_SIZE = 5


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

show_menu(window, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

pygame.display.set_caption("Game of Life by Lucas Mercier")

clock = pygame.time.Clock()

simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)


#Simulation Loop
while True:

    #1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life by Lucas Mercier - Running")

            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life by Lucas Mercier - Paused")

            elif event.key == pygame.K_ESCAPE:
                show_menu(window, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)
                

    #2. Updating State
    simulation.update()

    #3. Drawing
    window.fill(GREY) #background
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
