import pygame

class Box(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("./asset/cardboard_box_01.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(240, 550, 20, 20)

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += 3
        elif keys[pygame.K_a]:
            self.rect.x -= 3

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 450:
            self.rect.x = 450