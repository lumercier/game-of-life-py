import pygame, sys

pygame.font.init()
font_title = pygame.font.Font("Fonts\slkscr.ttf", 120)
font_button = pygame.font.Font("Fonts\slkscr.ttf", 60)
font_credit = pygame.font.Font("Fonts\slkscr.ttf", 40)
GREY = (20, 20 ,20)

# Menu
def show_menu(window, WINDOW_WIDTH, WINDOW_HEIGHT, FPS):

    pygame.display.set_caption("Game of Life by Lucas Mercier - Menu")

   
    #Titre & Crédits
    title_surface = font_title.render("Game of Life", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(WINDOW_WIDTH // 2, 300)) #300 = espacement à partir du haut

    credit_surface = font_credit.render("Lucas Mercier - v0.5", True, (255, 255, 255))
    credit_rect = credit_surface.get_rect(center=(WINDOW_WIDTH // 2, 950))

    #Boutons
    buttons = {
        "Play": pygame.Rect(WINDOW_WIDTH // 2.5 - 100, 500, 400, 70),
        "Options": pygame.Rect(WINDOW_WIDTH // 2.5 - 100, 580, 400, 70),
        "Quit": pygame.Rect(WINDOW_WIDTH // 2.5 - 100, 660, 400, 100)
    }

    
    clock = pygame.time.Clock()
    
    while True:
        window.fill((30,30,30))

        # Affichage du titre & Crédit
        window.blit(title_surface, title_rect)
        window.blit(credit_surface, credit_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for text, rect in buttons.items():
            # Vérifier si la souris survole le bouton
            color = (255, 128, 0) if rect.collidepoint(mouse_x, mouse_y) else (255, 255, 255)
            button_surface = font_button.render(text, True, color)
            button_rect = button_surface.get_rect(center=rect.center)

            pygame.draw.rect(window, GREY, rect, border_radius=10)
            window.blit(button_surface, button_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["Play"].collidepoint(mouse_x, mouse_y):
                    return  # Sort du menu et lance la simulation
                elif buttons["Quit"].collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        clock.tick(FPS)
