import pygame

class Goal:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.world_x = x

    def draw(self, screen, camera_offset):
        draw_rect = pygame.Rect(self.rect.x - camera_offset, self.rect.y, self.rect.width, self.rect.height)
        pygame.draw.rect(screen, (0, 255, 0), draw_rect)
