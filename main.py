import enum
import pygame
from sprites import *
from config import *
import sys
import tkinter as tk



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((win_width, win_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('BAUHS93.TTF', 70)

    
        

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')
        self.intro_background = pygame.image.load('./img/Backgrounds.png')
        self.go_background = pygame.image.load('./img/gameover.png')
        self.time_image = Spritesheet('img/time.png')
        self.water_image = Spritesheet('img/water.png')
        self.oak_image = Spritesheet('img/oak.png')
        self.spruce_image = Spritesheet('img/spruce.png')
        self.lava_image = Spritesheet('img/lava.png')
        self.grassdown_image = Spritesheet('img/grassdown.png')
        self.stonedown_image = Spritesheet('img/stonedown.png')
        self.stone_image = Spritesheet('img/stone.png')
        self.haydown_image = Spritesheet('img/terrain.png')
        self.hay_image = Spritesheet('img/terrain.png')
        self.forestgrassdown_image = Spritesheet('img/forestgrassdown.png')
        self.sakura_image = Spritesheet('img/sakura.png')
        self.forestgrass_image = Spritesheet('img/terrain.png')
        self.bridge1_image = Spritesheet('img/Bridge1.png')
        self.bridge2_image = Spritesheet('img/Bridge2.png')
        self.bridge3_image = Spritesheet('img/Bridge3.png')
        self.bridge4_image = Spritesheet('img/Bridge4.png')
        self.bridge5_image = Spritesheet('img/Bridge5.png')
        self.potion_image = Spritesheet('img/potion.png')
        self.house_spritesheet = Spritesheet('img/house.png')

        

    def create_tilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self,j,i)
                if column == "E":
                    Enemy(self, j,i)
                if column == "P":
                    self.player = Player(self,j,i)
                if column == "T":
                    Time(self,j,i)
                if column == "W":
                    Water(self,j,i)
                if column == "O":
                    Oak(self,j,i)
                if column == "S":
                    Spruce(self,j,i)
                if column == "L":
                    Lava(self,j,i)
                if column == "Z":
                    Grassdown(self,j,i)
                if column == "Y":
                    Stonedown(self,j,i)
                if column == "U":
                    Stone(self,j,i)
                if column == "I":
                    Haydown(self,j,i)
                if column == "H":
                    Hay(self,j,i)
                if column == "G":
                    Forestground(self,j,i)
                if column == "J":
                     Forestgrounddown(self,j,i)
                if column == "K":
                     Sakuratree(self,j,i)
                if column == "A":
                     Bridge1(self,j,i)
                if column == "M":
                     Bridge2(self,j,i)
                if column == "N":
                     Bridge3(self,j,i)
                if column == "Q":
                     Bridge4(self,j,i)
                if column == "R":
                     Bridge5(self,j,i)
                if column == "C":
                     Water2(self,j,i)
                if column == "D":
                    Potion(self,j,i)
                if column == "F":
                    House1(self,j,i)    
                if column == "V":
                    House2(self,j,i)    
                if column == "X":
                    House3(self,j,i)    
                if column == "à":
                    House4(self,j,i)    
                if column == "ä":
                    House5(self,j,i)
                if column == "é":
                    House6(self,j,i)
                if column == "ö":
                    House7(self,j,i)
                if column == "ü":
                    House8(self,j,i)
                if column == "è":
                    House9(self,j,i)
                    


    def new(self):
        
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.create_tilemap()

        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - tilesize)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + tilesize)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - tilesize, self.player.rect.y) 
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + tilesize, self.player.rect.y) 

    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(fps)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def game_over(self):
        text = self.font.render('Game over', True, WHITE)
        text_rect = text.get_rect(center=(win_width/2, win_height/2))

        restart_button = Button(10, win_height - 60, 120, 50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos,mouse_pressed):
                self.new()
                self.main()
                

            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(fps)
            pygame.display.update()
    

    


    def intro_screen(self):
        intro = True

        title = self.font.render('The Grand Adventure', True, BLACK)
        title_rect = title.get_rect(x=240, y=90)

        play_button = Button(500, 200, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(fps)
            pygame.display.update()
    






g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
