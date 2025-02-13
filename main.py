import pygame
import sys
import player
import spritesheet
from pytmx.util_pygame import load_pygame
import pokemon
import random

# Initialised the pygame library
pygame.init()



class Main_Game():
    def __init__(self, screen_width, screen_height, tile_size):
        # Here, declaring the screen 
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        self.tile_size = tile_size
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Adding the states
        self.game_speed = 20

        self.game_loop_state = False
        self.start_menu_state = True
        self.title_screen_state = True
        self.settings_state = False

        
        self.collision_sprites = pygame.sprite.Group()
        self.encounters = pygame.sprite.Group()
        self.all_sprites = spritesheet.Camera(self.screen)
        
        
        self.battle = False
        self.user_lost = False
        self.ran_away = False
        self.user_won = False
        self.character = "assets/character/red_walking.png"

    def start_menu(self,key_press):
        self.screen.fill('black')

        logo = spritesheet.Spritesheet('assets/logo.png').get_sprite(0,172, 104,3, (255,255,255))
        logo_rect = logo.get_rect(center=(640, 200))

    
        play_text = spritesheet.font_writing('Press Shift', "assets/dark_font.png")
        count = 0
        for text in play_text:
            self.screen.blit(text,((count+516),400) )
            count+=(6*4)
        
        self.screen.blit(logo, logo_rect)

        if key_press[pygame.K_LSHIFT] or key_press[pygame.K_RSHIFT]:
            self.start_menu_state = False
    
    def title_screen(self, key_press):
        
        self.screen.fill('black')
        save_text = spritesheet.font_writing('New Game    Press A', 'assets/dark_font.png')
        settings_text = spritesheet.font_writing('Settings    Press B', 'assets/dark_font.png')

        count = 0
        for text in save_text:
            self.screen.blit(text,((count+400),200) )
            count+=(6*4)
        count = 0
        for text in settings_text:
            self.screen.blit(text,((count+400),400) )
            count+=(6*4)

        if key_press[pygame.K_a]:
            self.character_state = True
            self.title_screen_state = False


        elif key_press[pygame.K_b]:
            self.settings_state = True
            self.title_screen_state = False
   
    def settings(self):

        self.screen.fill('black')

        key_press = pygame.key.get_pressed()
    
        text_speed_text = spritesheet.font_writing('Select Text Speed','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),150) )
            count+=(6*4)

        speed = {
            28: 'Slow',
            20: 'Fast'
        }
        current_speed = speed[self.game_speed]
        speed_options = spritesheet.font_writing(f"{current_speed}    Press A to change", 'assets/dark_font.png')
        count = 0
        for text in speed_options:
            self.screen.blit(text,((count+100),300) )
            count+=(6*4)

        exit_text = spritesheet.font_writing("Press Return to save", "assets/dark_font.png")
        count = 0
        for text in exit_text:
            self.screen.blit(text,((count+90),400) )
            count+=(6*4)


        if key_press[pygame.K_a]:
            if self.game_speed == 20:
                self.game_speed = 28
            else:
                self.game_speed = 20
        elif key_press[pygame.K_RETURN]:
            self.title_screen_state = True
            self.settings_state = False
            
    def male_or_female(self):
        text = spritesheet.font_writing("Press A for male", "assets/dark_font.png")
        count = 0
        for text in text:
            self.screen.blit(text,((count+90),200) )
            count+=(6*4)

        text = spritesheet.font_writing("Press B for female", "assets/dark_font.png")
        count = 0
        for text in text:
            self.screen.blit(text,((count+90),400) )
            count+=(6*4)

        text = spritesheet.font_writing("Press Return to continue", "assets/dark_font.png")
        count = 0
        for text in text:
            self.screen.blit(text,((count+90),600) )
            count+=(6*4)
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_b]:
            self.character = "assets/character/green_walking.png"
        elif keys[pygame.K_a]:
            self.character = "assets/character/red_walking.png"
        if keys[pygame.K_RETURN]:
            self.import_maps()
            self.setup(self.tmx_maps['world'], 'house')

            

            self.game_loop_state = True
            self.character_state = False


    def game_over(self, keys):
        self.screen.fill('black')
    
        text_speed_text = spritesheet.font_writing('Game Over','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),150) )
            count+=(6*4)
        
        text_speed_text = spritesheet.font_writing('Press Return to continue','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),300) )
            count+=(6*4)
        
        if keys[pygame.K_RETURN]:
            self.user_lost = False

    def ran(self, keys):
        self.screen.fill('black')
    
        text_speed_text = spritesheet.font_writing('You ran away','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),150) )
            count+=(6*4)
        
        text_speed_text = spritesheet.font_writing('Press Return to continue','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),300) )
            count+=(6*4)

        if keys[pygame.K_RETURN]:
            self.ran_away = False

    def user_win(self, keys):
        self.screen.fill('black')
    
        text_speed_text = spritesheet.font_writing('You won','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),150) )
            count+=(6*4)
        
        text_speed_text = spritesheet.font_writing('Press Return to continue','assets/dark_font.png' )
        count = 0
        for text in text_speed_text:
            self.screen.blit(text,((count+150),300) )
            count+=(6*4)

        if keys[pygame.K_RETURN]:
            self.user_won = False

    def import_maps(self):
        self.tmx_maps = {'world': load_pygame('assets/map/world.tmx')}
    
    def setup(self, tmx_map, player_start_pos):
        # for ground level
        for x,y, surf in tmx_map.get_layer_by_name('Ground').tiles():
            spritesheet.Tiles((x*self.tile_size,y*self.tile_size), surf, self.all_sprites)

        
        # for the upper ground level
        for x,y,surf in tmx_map.get_layer_by_name('Upper Ground').tiles():
            spritesheet.Tiles((x*self.tile_size,y*self.tile_size), surf, self.all_sprites)
        
        # for collisions
        for obj in tmx_map.get_layer_by_name('Collisions'):
            spritesheet.BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), (self.collision_sprites))

        # for the grass tiles
        for obj in tmx_map.get_layer_by_name('Grass'):
            spritesheet.Tiles((obj.x, obj.y), obj.image, (self.all_sprites, self.encounters))

        # for the entities
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['Position'] == player_start_pos:
                    self.x, self.y = obj.x, obj.y
                    self.user = player.Character(self.x, self.y,self.character, self.screen_width, self.screen_height, self.tile_size, self.collision_sprites)
            else:
                sprite = player.NPC(obj.x, obj.y, f'assets/character/{obj.name}.png', self.screen_width, self.screen_height, self.tile_size, self.collision_sprites)
                self.all_sprites.add(sprite)

    def game_loop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if self.start_menu_state:
                self.start_menu(keys)
            elif self.title_screen_state:
                self.title_screen(keys)
            elif self.settings_state:
                self.settings()
            elif self.character_state:
                self.male_or_female()

            elif self.battle:
                self.game_speed = 6
                self.battle.update(keys)
                battle_end, self.user_lost, self.user_won ,self.ran_away = self.battle.run(keys)
                if battle_end:
                    self.battle = False
                    self.game_speed = 20
            
            elif self.user_lost:
                self.game_over(keys)
            elif self.user_won:
                self.user_win(keys)
            elif self.ran_away:
                self.ran(keys)

            elif self.game_loop_state:
                    
                self.user.update(keys)
                encounter_rate = random.randint(1,100)
                if self.user.encounter_check(self.encounters) and encounter_rate == 6:
                    
                    self.user_pokemon = {
                        0: pokemon.Pokemon(random.choice(pokemon.id), 15),
                    }
                    self.dummy = {
                        0: pokemon.Pokemon(random.choice(pokemon.id), 10),
                    }
                    self.battle = pokemon.Battle(self.user_pokemon, self.dummy,pygame.image.load('assets/battle/battle_background.png') )
                
                self.all_sprites.draw((self.x, self.y))

                self.screen.blit(self.user.image, self.user.rect)
                self.x, self.y = self.user.rect.x, self.user.rect.y

                


            pygame.display.flip()

            clock.tick(self.game_speed)


        pygame.quit()
        sys.exit()



game = Main_Game(spritesheet.screen_width, spritesheet.screen_height, spritesheet.tile_size)
game.game_loop()
