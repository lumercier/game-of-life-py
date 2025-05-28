import pygame, sys
from menu import show_menu
import os
import sys


pygame.init() #ADDED
pygame.font.init()

#screen = pygame.display.set_mode((800, 600))

font_title = pygame.font.Font("Fonts/slkscr.ttf", 60)
font_button = pygame.font.Font("Fonts/slkscr.ttf", 30)
font_credit = pygame.font.Font("Fonts/slkscr.ttf", 40)
Background_color = (0, 0 ,0)

# Couleurs
WHITE = (30, 30, 30)
BLACK = (0, 0, 0)


# Menu
def show_menu2(window, WINDOW_WIDTH, WINDOW_HEIGHT, FPS):

    pygame.display.set_caption("Pause Menu")

    #Titre & Crédits
    title_surface = font_title.render("Pause Menu", True, (255, 255, 255), (0, 0, 0))
    title_rect = title_surface.get_rect(center=(WINDOW_WIDTH // 2, 100)) #300 = espacement à partir du haut

    credit_surface = font_credit.render("Lucas Mercier - v0.6", True, (255, 255, 255))
    credit_rect = credit_surface.get_rect(center=(WINDOW_WIDTH // 2, 950))

    #Boutons
    buttons = {
        "Resume": pygame.Rect(WINDOW_WIDTH // 2.5 - 100, 500, 400, 50),
        "Options": pygame.Rect(WINDOW_WIDTH // 2.5 - 100, 570, 400, 50),
        "Main Menu": pygame.Rect(WINDOW_WIDTH // 2.5 - 100, 640, 400, 50),
        "Quit": pygame.Rect(WINDOW_WIDTH // 2.5 - 100, 710, 400, 50)
    }

    # Texte explicatif
    instructions = [
        "COMMANDS :",
        "ENTER - Launch / resume",
        "SPACE - Pause the game",
        "S - Not implemented for now",
        "P - Not implemented for now",
        "ESCAPE - Pause menu"
    ]

    y_offset = 200  # Position de départ verticale
    for line in instructions:
        instruction_surface = font_button.render(line, True, (255, 255, 255), (0, 0, 0))
        instruction_rect = instruction_surface.get_rect(topleft=(100, y_offset))
        window.blit(instruction_surface, instruction_rect)
        y_offset += 40  # Espacement entre les lignes



    clock = pygame.time.Clock()
    
    while True:
        
        # Affichage du titre & Crédit
        window.blit(title_surface, title_rect)
        window.blit(credit_surface, credit_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for text, rect in buttons.items():
            # Vérifier si la souris survole le bouton
            color = (255, 128, 0) if rect.collidepoint(mouse_x, mouse_y) else (255, 255, 255)
            button_surface = font_button.render(text, True, color)
            button_rect = button_surface.get_rect(center=rect.center)

            pygame.draw.rect(window, Background_color, rect, border_radius=30)
            window.blit(button_surface, button_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["Resume"].collidepoint(mouse_x, mouse_y):
                    return  # Sort du menu et lance la simulation
                if buttons["Quit"].collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
                elif buttons["Main Menu"].collidepoint(mouse_x, mouse_y):
                    #pygame.quit()
                    #sys.exit()
                    #show_menu(window, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)
                    os.execv(sys.executable, ['python'] + sys.argv)  # Redémarre tout le script


        clock.tick(FPS)
