import pygame
from dino_runner.utils.constants import RUNNING,DUCKING,JUMPING
from pygame.sprite import Sprite

class Dinosaur (Sprite):
    X_POS = 80
    Y_POS = 310
    POS_Y_DUCKING = 345
    JUMP_VEL = 10

def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

def update(self, user_input):
    if user_input[pygame.K_DOWN]:
        self.duck()
    else:
         self.run()
    self.run()
    if self.step_index >= 10:
        self.step_index = 0

def draw(self, screen):
    screen.blit(self.image, self.dino_rect)
    
def run(self):
    self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
    self.dino_rect.x = self.POS_X
    self.dino_rect.y = self.POS_Y
    self.step_index += 1
    
def duck(self):
    pass

def jump(self):
     pass