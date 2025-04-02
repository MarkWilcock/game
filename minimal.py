## minimal example form ChatGPT

import pygame
import sys

# Initialize
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Basics")

# Player setup
player = pygame.Rect(300, 220, 50, 50)
player_color = (0, 255, 0)
speed = 5

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen (black)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed
    if keys[pygame.K_UP]:    player.y -= speed
    if keys[pygame.K_DOWN]:  player.y += speed

    # Draw player
    pygame.draw.rect(screen, player_color, player)

    # Update screen
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
