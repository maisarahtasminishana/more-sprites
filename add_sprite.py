import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rectangle Sprite Movement")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the dimensions of the rectangles
rect_width = 60
rect_height = 60

# Create two rectangles: one for player-controlled and one static
rect1_x, rect1_y = 100, 100  # Player-controlled rectangle (RED)
rect2_x, rect2_y = 500, 100  # Static rectangle (BLUE)

# Set the initial movement speed
speed = 5

# Create the game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Control movement of the first rectangle using arrow keys
    if keys[pygame.K_LEFT]:
        rect1_x -= speed
    if keys[pygame.K_RIGHT]:
        rect1_x += speed
    if keys[pygame.K_UP]:
        rect1_y -= speed
    if keys[pygame.K_DOWN]:
        rect1_y += speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw the rectangles on the screen
    pygame.draw.rect(screen, RED, (rect1_x, rect1_y, rect_width, rect_height))  # Player-controlled rectangle
    pygame.draw.rect(screen, BLUE, (rect2_x, rect2_y, rect_width, rect_height))  # Static rectangle

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
