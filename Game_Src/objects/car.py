import pygame.sprite
from layer import Layer
from objects.columns import Column
import assets
import configs



class Car(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER

        

        self.image = assets.get_sprite("rs6")
        self.rect = self.image.get_rect(topleft = (-100, 50))
        
        self.mask = pygame.mask.from_surface(self.image)

        self.flap = 0

        super().__init__(*groups)

    def update(self):
        self.flap += configs.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 3

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 6


    def check_colision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is Column) and sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or self.rect.bottom < 50 or self.rect.top > 750):
                return True
        return False