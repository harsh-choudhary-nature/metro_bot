
import pygame
import sys

pygame.init()

# Set up display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Basic Pygame Example')
# Load images
background = pygame.image.load('track.png').convert()
player = pygame.image.load('agent.jpg').convert()
# Rotate the player image
angle = -90  # Specify the angle of rotation
rotated_player = pygame.transform.rotate(player, angle)
start_pos = (100, 70)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background and player
    screen.blit(background, (0, 0))  # Draw background at (0,0)
    screen.blit(rotated_player, start_pos)  # Draw player at (200,200) - adjust as needed

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
