import csv
import pygame

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
    "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel",
    "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter",
    "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb",
    "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee",
    "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon",
    "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking",
    "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar",
    "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee",
    "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto",
    "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres",
    "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

class Pokemon:
    def __init__(self, name, level):
        self.name, self.level = name, level
        self.id = str(id.index(self.name))
        #stats
        self.type1 = pokemon_data[self.id]['Type1']
        self.type2 = pokemon_data[self.id]['Type2']
        self.attack = pokemon_data[self.id]['Attack']
        self.defense = pokemon_data[self.id]['Defense']
        self.spattack = pokemon_data[self.id]['Sp. Atk']
        self.spdefence = pokemon_data[self.id]['Sp. Def']
        self.speed = pokemon_data[self.id]['Speed']

class Battle:
    def __init__(self, user_pkmn, opp_pkmn, frames, bg, fonts):
        self.display_surface = pygame.display.get_surface()
        self.bg = bg
        self.frames = frames
        self.fonts = fonts
        self.pkmn_data = {'user':user_pkmn, 'opps':opp_pkmn}

    def update(self, dt):
        self.display_surface.blit(self.bg, (0,0))