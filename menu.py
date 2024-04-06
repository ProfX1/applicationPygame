import pygame
import sys
import json

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

# Fonction pour afficher les highscores
def show_highscores():
    # Chargement des highscores à partir d'un fichier
    try:
        with open('highscores.json', 'r') as f:
            highscores = json.load(f)
    except FileNotFoundError:
        highscores = []

    # Tri des highscores par score décroissant
    highscores.sort(key=lambda x: x['score'], reverse=True)

    # Affichage des highscores
    font = pygame.font.Font(None, 36)
    for i, score in enumerate(highscores[:10]):
        text = f"{i+1}. {score['name']} - {score['score']}"
        text_render = font.render(text, True, WHITE)
        screen.blit(text_render, (50, 50 + i * 40))


# Boucle principale
running = True
show_highscores_flag = False  # Définir un indicateur pour afficher les highscores

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le bouton "Highscores" est cliqué
            if 250 < event.pos[0] < 350 and 180 < event.pos[1] < 220:
                show_highscores_flag = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Retour au menu principal
                show_highscores_flag = False


    # Remplissage de l'écran
    screen.fill((50, 50, 50))

    # Dessin des boutons du menu principal
    draw_button('Nouvelle Partie', (300, 100))
    draw_button('Highscores', (300, 200))
    draw_button('Quitter', (300, 300))

    # Si le drapeau pour afficher les highscores est vrai, afficher les highscores
    if show_highscores_flag:
        show_highscores()

    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()