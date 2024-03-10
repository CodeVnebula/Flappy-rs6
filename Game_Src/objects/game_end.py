import pygame.sprite
from layer import Layer
import assets
import configs

class GameOverMsg(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.image = assets.get_sprite("over")
        self.rect = self.image.get_rect(center = (configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2))
        super().__init__(*groups)