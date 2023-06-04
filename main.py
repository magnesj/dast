import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Example")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw a white rectangle in the center
    rect_width, rect_height = 200, 100
    rect_x = (width - rect_width) // 2
    rect_y = (height - rect_height) // 2
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

