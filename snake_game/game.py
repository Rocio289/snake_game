## Clase Game (para la lógica general del juego)

import pygame
from snake import Snake
from fruit import Fruit
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.snake = Snake()
        self.fruit = Fruit()
        self.running = True

    def check_collision(self):
        if self.snake.body[0] == self.fruit.position:
            self.snake.grow()
            self.fruit = Fruit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -20))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 20))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-20, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((20, 0))

    def update(self):
        self.snake.move()
        self.check_collision()

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.fruit.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)

        pygame.quit()