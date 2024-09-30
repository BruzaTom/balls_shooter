import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroid_field import AsteroidField
from shot import Shot
from logic import Logic
from background import Bg
from star import Star
#added from ball script
from circleshape2 import CircleShape2
from border import Border
from ball import Ball
import random

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sounds/myheadisempty.mp3')
pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play(start=0)

def main():
    clock = pygame.time.Clock()
    dt = 0
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    #groups
    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    asteroidsGroup = pygame.sprite.Group()
    shotsGroup = pygame.sprite.Group()
    #fill class containers
    Asteroid.containers = (asteroidsGroup, updatableGroup, drawableGroup)
    AsteroidField.containers = (updatableGroup)
    Shot.containers = (shotsGroup)
    Player.containers = (updatableGroup, drawableGroup)
    Logic.containers = (updatableGroup, drawableGroup)
    Bg.containers = (updatableGroup)
    Star.containers = (updatableGroup, drawableGroup)
    #added from ball script
    borderGroup = pygame.sprite.Group()
    ballGroup = pygame.sprite.Group()
    Border.containers = (borderGroup, drawableGroup, updatableGroup)
    Ball.containers = (ballGroup, drawableGroup, updatableGroup)
    #create objects
    field = AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2.5) + (SCREEN_HEIGHT / 2))
    ship.rotation = 180
    gamelogic = Logic()
    background = Bg()
    #added from ball script
    #border = Border(SCREEN_WIDTH / 2, BORDER_POS_Y)
    
    balls = 1
    while(True):
        if gamelogic.restart == True:
            return restart(gamelogic)
        screen.fill('Black')        
        for item in updatableGroup:
            item.update(dt)
        for item in sorted(drawableGroup, key = lambda object: object.priority, reverse = True):
        #for item in drawableGroup:
            item.draw(screen)
        for item in ballGroup:
            for shot in shotsGroup:
                if shot.collisions(item):
                    shot.kill()
                    item.bounce(balls)
                    gamelogic.score += 10
                    balls += 1
            if ship.collisions(item):
                print('Game over!')
                ship.dead = True
                gamelogic.gameover = True
            
        for item in shotsGroup:
            item.draw(screen)
            item.update(dt)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.display.update()#dont ever forget

def restart(gamelogic):
    gamelogic.restart = False
    main()
    

if __name__ == "__main__":
    main()