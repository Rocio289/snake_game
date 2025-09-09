## Clase Fruit

import pygame
import random
from config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

class Fruit:
    def __init__(self):
        self.position = self.random_position()
        self.image = pygame.image.load("assets/fruit.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

    def draw(self, screen):
        fruit_rect = pygame.Rect(
            self.position[0] * BLOCK_SIZE,
            self.position[1] * BLOCK_SIZE,
            BLOCK_SIZE, BLOCK_SIZE
        )
        screen.blit(self.image, fruit_rect)

    def random_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)