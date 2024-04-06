import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 1700, 1500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click Game")


#defime ball
ball = pygame.image.load("applicationPygame\\image\\balle.png")
ballrect = ball.get_rect()
speed = [8, 8]

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Define square parameters
SQUARE_SIZE = 50
square_color1 = BLACK
square_color2 = GRAY
score = 0
font = pygame.font.Font(None, 36)
time_limit = 30
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
                    score += 1
                    square1_x, square1_y = reset_square1()
                elif square2_x < mouse_x < square2_x + SQUARE_SIZE and square2_y < mouse_y < square2_y + SQUARE_SIZE:
                    score -= 1
                    square2_x, square2_y = reset_square2()
            elif event.button == 3:  # Right mouse button
                if square1_x < mouse_x < square1_x + SQUARE_SIZE and square1_y < mouse_y < square1_y + SQUARE_SIZE:
                    score -= 1
                    square1_x, square1_y = reset_square1()
                elif square2_x < mouse_x < square2_x + SQUARE_SIZE and square2_y < mouse_y < square2_y + SQUARE_SIZE:
                    score += 1
                    square2_x, square2_y = reset_square2()
    


    # Draw square
    pygame.draw.rect(screen, square_color1, (square1_x, square1_y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, square_color2, (square2_x, square2_y, SQUARE_SIZE, SQUARE_SIZE))

        #move the ball around
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        speed[1] = -speed[1]
    screen.blit(ball, ballrect)

    # Display score
    draw_text(screen, f"Score: {score}", 10, 10)

    # Display remaining time
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    remaining_time = max(time_limit - elapsed_time, 0)
    draw_text(screen, f"Time: {remaining_time}", 10, 50)

    # Check if time is up
    if remaining_time <= 0:
        name = input("Enter your name: ")
        print(f"Your final score is: {score}!")
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
