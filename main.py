import pygame
from sprites import *
from config import *
import sys

class Game:
    def__init__(self) :
    pygame.init()
    self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font("Arial, 32")
    self.running = True


def new(self):
    # a new game starts
    self.playing = True

    self.all_sprites = pygame.sprite.LayeredUpdates()
    self.blocks = pygame.sprite.LayeredUpdates()
    self.enemies = pygame.sprite.LayeredUpdates()
    self.attacks = pygame.sprite.LayeredUpdates()


    self.player = player()


def update(self):

def draw(self):

def main(self):

def game_over(self):

def intro_screen(self):




