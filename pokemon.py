import csv
import pygame
import spritesheet


with open("pokemon_data.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the first row as headers
    pokemon_data = {row[0]: dict(zip(headers[1:], row[1:])) for row in reader}  # Key is the first column


id = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata",
    "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu",
    "Sandshrew", "Sandslash", "NidoranF", "Nidorina", "Nidoqueen", "NidoranM",
    "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales",
    "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume",
    "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth",
    "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine",
    "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
    "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke",
    "Slowbro", "Magnemite", "Magneton", "Farfetchd", "Doduo", "Dodrio", "Seel",
    "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter",
    "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb",
    "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee",
    "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon",
    "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking",
    "Staryu", "Starmie", "Mr Mime", "Scyther", "Jynx", "Electabuzz", "Magmar",
    "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee",
    "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto",
    "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres",
    "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

class Pokemon:
    def __init__(self, name, level):
        self.name, self.level = name, level
        self.id = str(id.index(self.name)+1)
        
        #stats
        self.type1 = pokemon_data[self.id]['Type1']
        self.type2 = pokemon_data[self.id]['Type2']
        self.hp = ((int(pokemon_data[self.id]['HP'])*self.level)/50)+10+self.level
        self.attack = ((int(pokemon_data[self.id]['Attack'])+self.level)/50)+5
        self.defense = ((int(pokemon_data[self.id]['Defense'])+self.level)/50)+5
        self.spatk = ((int(pokemon_data[self.id]['Sp. Atk'])+self.level)/50)+5
        self.spdef = ((int(pokemon_data[self.id]['Sp. Def'])+self.level)/50)+5
        self.speed = ((int(pokemon_data[self.id]['Speed'])+self.level)/50)+5

    def sprites(self):
        row = (int(self.id)-1) //15
        column = (int(self.id)-1)%15
        self.sprite_loc = spritesheet.Spritesheet('assets/pokemon_sprites.png')
        self.sprite = self.sprite_loc.pkmn_sprite(column, row)
        return self.sprite





class Battle:
    def __init__(self, user_pkmn, opp_pkmn, bg):
        self.display_surface = pygame.display.get_surface()
        self.bg = bg
        self.bg = pygame.transform.scale(self.bg,((240 * 5.5), (112* 5)))
        self.user_sprites = []
        for i in user_pkmn:
            self.user_sprites.append(user_pkmn[i].sprites())
        self.opp_sprites = []
        for i in opp_pkmn:
            self.opp_sprites.append(opp_pkmn[i].sprites())

        self.pkmn_data = {'user':user_pkmn, 'opps':opp_pkmn}
        
        user_health, opp_health = self.pkmn_data['user'][0].hp, self.pkmn_data['opps'][0].hp
        self.user_hp = user_health
        self.opp_hp = opp_health

        self.default_state = True
        self.fight_state = False
        self.run_state = False

    def update(self, keys):
        # Displays the background and the bottom label
        self.display_surface.blit(self.bg, (0,0))
        self.display_surface.blit(pygame.transform.scale(pygame.image.load('assets/battle/text_box.png'),((240 * 5.4), (48* 3))), (0,560))
        self.display_surface.blit(self.user_sprites[0], (275, 350))
        self.display_surface.blit(self.opp_sprites[0], (800, 150))

       

        if self.default_state:
            self.default(keys)
        elif self.fight_state:
            self.fight()
        elif self.run_state:
            self.run()


    def default(self, keys):
        # the name boxes
        name_box = spritesheet.Spritesheet('assets/battle/name_box.png')
        self.display_surface.blit(name_box.name_box(),(25, 15))
        self.display_surface.blit(name_box.name_box(), (750, 350))

        # for the names of the pokemon
        name = spritesheet.font_writing(f'{self.pkmn_data['user'][0].name}', "assets/light_font.png")
        count = 0
        for text in name:
            self.display_surface.blit(text,((count+810),395) )
            count+=(6*4)        
        
        name = spritesheet.font_writing(f'{self.pkmn_data['opps'][0].name}', "assets/light_font.png")
        count = 0
        for text in name:
            self.display_surface.blit(text,((count+100),55) )
            count+=(6*4) 


        # For the text at the bottom
        play_text = spritesheet.font_writing('Fight                 Run', "assets/dark_font.png")
        count = 0
        for text in play_text:
            self.display_surface.blit(text,((count+150),595) )
            count+=(6*4)

        play_text = spritesheet.font_writing('Press A               Press B', 'assets/dark_font.png')
        count = 0
        for text in play_text:
            self.display_surface.blit(text,((count+200),640) )
            count+=(6*4)

        self.hp(self.user_hp/2, self.pkmn_data['user'][0].hp, (960,450))
        self.hp(self.opp_hp, self.pkmn_data['opps'][0].hp, (235,115))


        if keys[pygame.K_a]:
            self.fight_state = True
            self.default_state = False
        elif keys[pygame.K_b]:
            self.run_state = True
            self.default_state = False

    def run(self):
        del self
    
    def fight(self):
        moves = []
        for move in self.pkmn_data['user'].moves():
            moves.append(move.name)

    def hp(self, c_health, t_health, pos):
        total_hp = t_health
        current_hp = c_health
        remaining = current_hp/total_hp

        if remaining >0.5:
            bg_color = 'green'
        elif remaining >0.25:
            bg_color = 'yellow'
        else:
            bg_color = 'red'
        
        # Calculate HP percentage
        current_bar_width = int(240 * remaining)

        # Draw HP bar (if HP > 0)
        if current_hp > 0:
            pygame.draw.rect(self.display_surface, bg_color, (pos[0], pos[1], current_bar_width, 15))

        