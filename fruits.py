import random
import pygame

class Fruits(pygame.sprite.Sprite):



    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("./asset/fruta1.png")
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = self.image.get_rect()

        self.rect.x = 0 + random.randint(1,450)
        self.rect.y = 0

        self.speed = 1 + random.random() * 2

    def update(self, *args):
        self.rect.y += self.speed

