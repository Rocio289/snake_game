## Clase Fruit

import pygame
import random
from config import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Fruit:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))