import sys
import pygame
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

# Code pour la balle qui va rebondir
size = width, height = 1700, 1500
speed = [8, 8]
black = 0, 0, 0
clock = pygame.time.Clock()
ball = pygame.image.load("applicationPygame\\image\\balle.png")
ballrect = ball.get_rect()

# Boucle principale
running = True
show_highscores_flag = False  # Définir un indicateur pour afficher les highscores
new_game_flag = False  # Définir un indicateur pour démarrer un nouveau jeu

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le bouton "Highscores" est cliqué
            if 250 < event.pos[0] < 350 and 180 < event.pos[1] < 220:
                show_highscores_flag = True
            # Vérifier si le bouton "Nouvelle Partie" est cliqué
            elif 250 < event.pos[0] < 350 and 80 < event.pos[1] < 120:
                new_game_flag = True
                show_highscores_flag = False  # Masquer les highscores lorsque vous démarrez une nouvelle partie
            # Vérifier si le bouton "Quitter" est cliqué
            elif 250 < event.pos[0] < 350 and 280 < event.pos[1] < 320:
                pygame.quit()  # Quitter Pygame
                sys.exit()     # Quitter le script

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Retour au menu principal
                show_highscores_flag = False
                new_game_flag = False

    # Remplissage de l'écran
    screen.fill((50, 50, 50))

    # Dessin des boutons du menu principal uniquement si new_game_flag est False
    if not new_game_flag:
        draw_button('Nouvelle Partie', (300, 100))
        draw_button('Highscores', (300, 200))
        draw_button('Quitter', (300, 300))

    # Si le drapeau pour afficher les highscores est vrai, afficher les highscores
    if show_highscores_flag:
        show_highscores()

    # Si le drapeau pour démarrer une nouvelle partie est vrai, dessiner la balle
    if new_game_flag:
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        screen.blit(ball, ballrect)

    # Mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(60)

# Quitter Pygame (cette partie ne sera jamais atteinte mais c'est une bonne pratique)
pygame.quit()
sys.exit()