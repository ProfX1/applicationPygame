import sys
import pygame
import json
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
RED = (255, 0, 0)
WHITE = (255, 255, 255)
score_colors = [(255, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 128, 128), (128, 0, 0), (0, 128, 0)]

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
        with open('applicationPygame\\highscores.json', 'r') as f:
            highscores = json.load(f)
    except FileNotFoundError:
        highscores = []

    # Tri des highscores par score décroissant
    highscores.sort(key=lambda x: x['score'], reverse=True)

    # Affichage des highscores
    font = pygame.font.Font(None, 36)
    line_height = 40  # Définir la hauteur de ligne constante entre chaque score
    for i, score in enumerate(highscores[:10]):
        # Sélectionner une couleur de la liste pour ce score
        color = score_colors[i % len(score_colors)]
        text = f"{i+1}. {score['nom']} - {score['score']}"
        text_render = font.render(text, True, color)  # Utiliser la couleur sélectionnée
        screen.blit(text_render, (50, 50 + i * line_height))

# Fonction pour saisir le nom du joueur et enregistrer le score
def save_score(score, name):
    
    new_score = {'nom': name, 'score': score}
    try:
        with open('applicationPygame\\highscores.json', 'r') as f:
            highscores = json.load(f)
    except FileNotFoundError:
        highscores = []
    highscores.append(new_score)
    with open('applicationPygame\\highscores.json', 'w') as f:
        json.dump(highscores, f)

# Code pour la balle qui va rebondir
size = width, height = 1700, 1500
speed = [8, 8]
black = 0, 0, 0
clock = pygame.time.Clock()
ball = pygame.image.load("applicationPygame\\image\\balle.png")
ballrect = ball.get_rect()

# Définir le code pour le jeu
def game_code():
    # Set up the screen
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Click Game")

    # Define ball
    ball = pygame.image.load("applicationPygame\\image\\balle.png")
    # Define the scale factor for resizing (e.g., 0.5 for half the size)
    scale_factor = 0.25

    # Resize the ball image
    resized_ball = pygame.transform.scale(ball, (int(ball.get_width() * scale_factor), int(ball.get_height() * scale_factor)))

    # Get the rectangle of the resized ball
    ballrect = resized_ball.get_rect()
    # ballrect = ball.get_rect()
    speed = [8, 8]

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)

    # Define square parameters
    SQUARE_SIZE = 50
    square_color1 = BLUE
    square_color2 = RED
    score = 0
    font = pygame.font.Font(None, 36)
    time_limit = 20
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # Function to display text
    def draw_text(surface, text, x, y):
        text_surface = font.render(text, True, BLACK)
        surface.blit(text_surface, (x, y))

    # Function to reset square position
    def reset_square1():
        x = random.randint(0, WIDTH - SQUARE_SIZE)
        y = random.randint(0, HEIGHT - SQUARE_SIZE)
        return x, y

    def reset_square2():
        x = random.randint(0, WIDTH - SQUARE_SIZE)
        y = random.randint(0, HEIGHT - SQUARE_SIZE)
        return x, y

    # Initial square position
    square1_x, square1_y = reset_square1()
    square2_x, square2_y = reset_square2()

    # Main game loop
    running = True
    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.button == 1:  # Left mouse button
                    if square1_x < mouse_x < square1_x + SQUARE_SIZE and square1_y < mouse_y < square1_y + SQUARE_SIZE:
                        if ballrect.collidepoint(mouse_x, mouse_y):
                            score -= 10  # reduce score if clicked on the ball
                        else:
                            score += 10
                            square1_x, square1_y = reset_square1()
                    elif square2_x < mouse_x < square2_x + SQUARE_SIZE and square2_y < mouse_y < square2_y + SQUARE_SIZE:
                        if ballrect.collidepoint(mouse_x, mouse_y):
                            score -= 10  # reduce score if clicked on the ball
                        else:
                            score -= 5
                            square2_x, square2_y = reset_square2()
                    elif ballrect.collidepoint(mouse_x, mouse_y):
                        score -= 10  # reduce score if clicked on the ball
                elif event.button == 3:  # Right mouse button
                    if square1_x < mouse_x < square1_x + SQUARE_SIZE and square1_y < mouse_y < square1_y + SQUARE_SIZE:
                        if ballrect.collidepoint(mouse_x, mouse_y):
                            score -= 10  # reduce score if clicked on the ball
                        else:
                            score -= 5
                            square1_x, square1_y = reset_square1()
                    elif square2_x < mouse_x < square2_x + SQUARE_SIZE and square2_y < mouse_y < square2_y + SQUARE_SIZE:
                        if ballrect.collidepoint(mouse_x, mouse_y):
                            score -= 10  # reduce score if clicked on the ball
                        else:
                            score += 10
                            square2_x, square2_y = reset_square2()
                    elif ballrect.collidepoint(mouse_x, mouse_y):
                        score -= 10  # reduce score if clicked on the ball


        # Draw square
        pygame.draw.rect(screen, square_color1, (square1_x, square1_y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(screen, square_color2, (square2_x, square2_y, SQUARE_SIZE, SQUARE_SIZE))

        # Move the ball around
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > WIDTH:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > HEIGHT:
            speed[1] = -speed[1]
        screen.blit(resized_ball, ballrect)

        # Display score
        draw_text(screen, f"Score: {score}", 10, 10)

        # Display remaining time
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) // 1000
        remaining_time = max(time_limit - elapsed_time, 0)
        draw_text(screen, f"Time: {remaining_time}", 10, 50)

        # Check if time is up
        if remaining_time <= 0:
            
            running = False  # End game
            def text_input():
                text = ""
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                return text
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode

                    screen.fill(WHITE)
                    draw_text("Enter your name:", font, BLACK, (50, 50))
                    draw_text(text, font, BLACK, (50, 100))
                    pygame.display.flip()

            # Function to draw text on the screen
            def draw_text(text, font, color, position):
                text_surface = font.render(text, True, color)
                screen.blit(text_surface, position)

            # Main loop
            def main():
                name = text_input()
                save_score(score, name)  # Call function to save score

            if __name__ == "__main__":
                main()


        pygame.display.flip()
        clock.tick(60)

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
                new_game_flag = False  # Assurez-vous que new_game_flag est défini sur False lorsque vous affichez les highscores
            # Vérifier si le bouton "Nouvelle Partie" est cliqué
            elif 250 < event.pos[0] < 350 and 80 < event.pos[1] < 120:
                new_game_flag = True
                show_highscores_flag = False  # Masquer les highscores lorsque vous démarrez une nouvelle partie
                game_code()  # Appeler la fonction game_code pour démarrer le jeu
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

    # Dessin des boutons du menu principal uniquement si new_game_flag est False et show_highscores_flag est False
    if not new_game_flag and not show_highscores_flag:
        draw_button('Nouvelle Partie', (300, 100))
        draw_button('Highscores', (300, 200))
        draw_button('Quitter', (300, 300))

    # Si le drapeau pour afficher les highscores est vrai, afficher les highscores
    if show_highscores_flag:
        show_highscores()
    pygame.display.flip()

# Quitter Pygame (cette partie ne sera jamais atteinte mais c'est une bonne pratique)
pygame.quit()
sys.exit()
