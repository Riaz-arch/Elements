import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
WHITE, BLUE = (255, 255, 255), (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Screen")
font = pygame.font.Font(None, 74)
text_surface = font.render("Hello, Pygame!", True, BLUE)

rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 100) // 2, 200, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, rect)
    screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, rect.bottom + 20))
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)