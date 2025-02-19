import random

import pygame

from box import Box
from fruits import Fruits
from stone import Stone

pygame.init()
tela = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Pegue as frutas!")

#objects
objectGroup = pygame.sprite.Group()
fruitGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()

#backgorund
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("./asset/sky1.png")
bg.image = pygame.transform.scale(bg.image, [500, 600])
bg.rect = bg.image.get_rect()

#music
pygame.mixer.music.load("./asset/Caketown 1.mp3")
pygame.mixer.music.play(-1)


gameloop = True
timer = 20
pontos = 0
clock = pygame.time.Clock()


box = Box(objectGroup)
fruta = Fruits(objectGroup, fruitGroup)
stone = Stone(objectGroup, obstacleGroup)

if __name__ == '__main__':
    while gameloop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False


        #logica
        objectGroup.update()
        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.5:
                newFruit = Fruits(objectGroup, fruitGroup)
            elif random.random() < 0.4:
                newStone = Stone(objectGroup, obstacleGroup)

        collisionsFruit = pygame.sprite.spritecollide(box, fruitGroup, True)
        collisionsObstacle = pygame.sprite.spritecollide(box, obstacleGroup, True)

        if collisionsObstacle:
           for stone in collisionsObstacle:
                stone.kill()
                print("Game over")
                gameloop = False
        elif collisionsFruit:
            pygame.mixer_music.load("./asset/cloth-inventory.wav")
            pygame.mixer_music.play(1)
            fruta.kill()
            pontos += 1

        #draw
        objectGroup.draw(tela)

        fonte = pygame.font.Font(None, 28)
        texto_pontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
        tela.blit(texto_pontos, (10, 10))

        box.update()
        fruta.update()
        stone.update()

        pygame.display.update()


