import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Menu du Jeu')

# Fonction pour dessiner un bouton
def draw_button(text, position):
    font = pygame.font.Font(None, 36)
    text_render = font.render(text, True, WHITE)
    text_rect = text_render.get_rect(center=position)
    pygame.draw.rect(screen, RED, text_rect.inflate(20, 10))
    screen.blit(text_render, text_rect)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplissage de l'écran
    screen.fill((50, 50, 50))

    # Dessin des boutons
    draw_button('Nouvelle Partie', (300, 100))
    draw_button('Highscores', (300, 200))
    draw_button('Quitter', (300, 300))

    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()