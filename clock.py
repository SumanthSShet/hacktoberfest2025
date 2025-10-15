import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Basic Game")
clock = pygame.time.Clock()
player_pos = [200, 150]
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= speed
    if keys[pygame.K_RIGHT] and player_pos[0] < 400:
        player_pos[0] += speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= speed
    if keys[pygame.K_DOWN] and player_pos[1] < 300:
        player_pos[1] += speed
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), player_pos, 20)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
