import pygame

from objects.background import Background
from objects.columns import Column
from objects.car import Car
from objects.game_start import GameStartMsg
from objects.game_end import GameOverMsg
from objects.score import Score
import configs
import assets

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
gameover = False
gamestarted = False


assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
    Background(0, sprites)
    Background(1, sprites)

    return Car(sprites), GameStartMsg(sprites), Score(sprites)

 
car, game_start_msg, score = create_sprites()





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                game_start_msg.kill()
                pygame.time.set_timer(column_create_event, 2200)
            if event.key ==pygame.K_ESCAPE and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                car, game_start_msg, score = create_sprites()

        car.handle_event(event)

    
    screen.fill(0)

    sprites.draw(screen)

    if gamestarted and not gameover:
        sprites.update()

    if car.check_colision(sprites):
        gameover = True
        gamestarted = False
        GameOverMsg(sprites)
        pygame.time.set_timer(column_create_event, 0)


    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1

    



    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()