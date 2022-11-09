import pygame
import numpy

pygame.init()
screen = pygame.display.set_mode([700, 700])

running = True
grid = numpy.random.randint(1, size=(70, 70))
grid[34,35] = 1
grid[34,34] = 1
grid[35,35] = 1
grid[35,36] = 1
grid[36,35] = 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface = pygame.surfarray.make_surface(grid)
    surface = pygame.transform.scale(surface, (700, 700))
    screen.fill((0, 0, 0))
    screen.blit(surface, (0, 0))
    pygame.display.flip()


pygame.quit()
