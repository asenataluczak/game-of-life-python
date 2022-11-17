from typing import Tuple
import pygame


class Button:

    def __init__(self, x, y, size, colors: Tuple[Tuple[int,int,int]], icon, backup_icon=""):
        self.x = x
        self.y = y
        self.size = size
        self.main_color = colors[0]
        self.background_color = colors[1]
        self.hover_color = colors[2]
        self.icon = icon
        self.backup_icon = backup_icon

    def draw(self, surface):
        pygame.draw.rect(surface, self.main_color,
                         (self.x, self.y, self.size, self.size), self.size, 5)
        self._draw_background(surface)
        surface.blit(self.icon, (self.x, self.y))

    def collide(self, mouse):
        return self.x <= mouse[0] <= self.x + self.size and self.y <= mouse[1] <= self.y + self.size

    def switch(self, surface, switched=False):
        self._draw_background(surface)
        if(switched and self.backup_icon):
            surface.blit(self.backup_icon, (self.x, self.y))
        else:
            surface.blit(self.icon, (self.x, self.y))

    def _draw_background(self, surface):
        pygame.draw.rect(surface, self.background_color,
                         (self.x+2, self.y+2, self.size-4, self.size-4), self.size-4, 5)


