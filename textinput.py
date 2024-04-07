import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Text input function
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
    print("You entered:", name)

if __name__ == "__main__":
    main()
