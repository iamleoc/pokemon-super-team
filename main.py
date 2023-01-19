"""
Author: Leo Clough
Description: This code will put together a team of Pokemon from any game such that you
will always have a type advantage over any opposing pokemon.
"""
# ----------------------------- SET UP -----------------------------
from pokedexes import * 
import type_advantages
import random

pokedex_choices = {
    "kanto": ["red", "blue", "yellow", "fire red", "leaf green"],
    "johto": ["gold", "silver", "crystal"],
    "hoenn": ["ruby", "sapphire", "emerald"],
    "sinnoh": ["diamond", "pearl"],
    "sinnoh_extended": ["platinum"],
    "johto_extended": ["heart gold", "soul silver"],
    "unova": ["black", "white"],
    "unova_extended": ["black 2", "white 2"],
    "kalos": ["x", "y"],
    "hoenn_extended": ["omega ruby", "alpha sapphire"],
    "alola": ["sun", "moon"],
    "alola_extended": ["ultra sun", "ultra moon"],
    "galar": ["sword", "shield"]
}

pokedex_mapping = {
    "kanto": kanto,
    "johto": johto,
    "hoenn": hoenn,
    "sinnoh": sinnoh,
    "sinnoh_extended": sinnoh_extended,
    "johto_extended": johto_extended,
    "unova": unova,
    "unova_extended": unova_extended,
    "kalos": kalos,
    "hoenn_extended": hoenn_extended,
    "alola": alola,
    "alola_extended": alola_extended,
    "galar": galar
}
# ----------------------------- FUNCTIONS -----------------------------

def remove_legendaries(pokedex):
    for legendary in legendaries:
        if legendary in pokedex:
            pokedex.pop(legendary)
    return pokedex
    
def get_pokedex(game):
    pokedex = ""
    pokedex += [k for k, v in pokedex_choices.items() if game in v][0]
    if pokedex:
        chosen_pokedex = pokedex_mapping[pokedex]
        return chosen_pokedex
    else:
        return False

def type_advantage_selection(game):
    """
    Determines which types and type advantage charts to use.
    It's important to use the variable 'game' in the first statement, and 'pokedex' in the next.
    This is because Fire Red and Leaf Green use the Kanto dex, but have different types and type advantages.
    """
    if game in ["red", "blue", "yellow"]:
        types = type_advantages.gen1_types
        type_chart = type_advantages.gen1_twice_as_effective
    elif pokedex in ["johto", "hoenn", "sinnoh", "kanto", "unova", "unova_extended"]:
        types = type_advantages.gen2to5_types
        type_chart = type_advantages.gen2to5_twice_as_effective
    else:
        types = type_advantages.gen6on_types
        type_chart = type_advantages.gen6on_twice_as_effective
    return types, type_chart

def user_choices():
    print("""
    ______         _  
    | ___ \       | |                                                      
    | |_/ /  ___  | | __  ___  _ __ ___    ___   _ __                      
    |  __/  / _ \ | |/ / / _ \| '_ ` _ \  / _ \ | '_ \                     
    | |    | (_) ||   < |  __/| | | | | || (_) || | | |                    
    \_|     \___/ |_|\_\ \___||_| |_| |_| \___/ |_| |_|                    
   _____                          ______         _  _      _             
  |_   _|                         | ___ \       (_)| |    | |            
    | |    ___   __ _  _ __ ___   | |_/ / _   _  _ | |  __| |  ___  _ __ 
    | |   / _ \ / _` || '_ ` _ \  | ___ \| | | || || | / _` | / _ \| '__|
    | |  |  __/| (_| || | | | | | | |_/ /| |_| || || || (_| ||  __/| |   
    \_/   \___| \__,_||_| |_| |_| \____/  \__,_||_||_| \__,_| \___||_| 

    """)
    print("Please choose a game from the following list: \n"
      "Gen I: red, blue, yellow \n"
      "Gen II: gold, silver, crystal \n"
      "Gen III: ruby, sapphire, emerald, fire red, leaf green \n"
      "Gen IV: diamond, pearl, platinum, heart gold, soul silver \n"
      "Gen V: black, white, black 2, white 2 \n"
      "Gen VI: x, y, omega ruby, alpha sapphire \n"
      "Gen VII: sun, moon, ultra sun, ultra moon \n"
      "Gen VIII: sword, shield")

    game = input("What game are you playing? ")
    pokedex = get_pokedex(game)
    if not pokedex:
        print("Please choose a game from the list.\n")
        user_choices()
    
    starter_pokemon = ""
    use_starter = input("Do you want to use your starter Pokemon? Y or N: ").upper()
    if use_starter == "Y":
        starter_pokemon = input("Who is your starter? Enter the most evolved form: ").lower()

    useLegendaries = input("Do you want to include legendary Pokemon in your team? Y or N: ").upper()

    return game, use_starter, starter_pokemon, useLegendaries, pokedex

# def fill_team(team, pokedex):
#     while len(team) < 6:
#         pokemon = random.choice(list(pokedex))
#         team.append(pokemon)
#     return team

# def super_effective_check(types, team_types, type_chart):
#     types_effective_against = set()
#     for type in team_types:
#         for pokemon_type in type_chart[type]:
#             types_effective_against.add(pokemon_type)
#     if types.issubset(types_effective_against):
#         return True
#     else:
#         super_effective_check(types, team_types, type_chart)

def create_team(_use_starter, _starter_pokemon, _useLegendaries, _pokedex, _types, _type_chart):
    team = [] 

    if _use_starter == "Y":
        team.append(_starter_pokemon)
    if _useLegendaries == "N":
        _pokedex = remove_legendaries(_pokedex)

    # create a weak_to pokedex
    weak_to_pokemon = {}
    for pokemon, attack_types in _pokedex.items():
        for attack_type in attack_types:
            for defense_type in _type_chart[attack_type]:
                weak_to_pokemon.setdefault(defense_type, []).append(pokemon)

    uncovered_types = sorted(weak_to_pokemon.items())
    uncovered_types = [(defense_type, strong_pokemons) for defense_type, strong_pokemons in uncovered_types if _starter_pokemon not in strong_pokemons]

    while uncovered_types and len(team) < 6:
        defense_type, candidates = uncovered_types[0]
        new_pokemon = random.choice(candidates)
        uncovered_types = [(defense_type, strong_pokemons) for defense_type, strong_pokemons in uncovered_types if new_pokemon not in strong_pokemons]
        team.append(new_pokemon)
    
    if len(team) < 6:
        team.extend(random.sample([pokemon for pokemon in _pokedex if pokemon not in team], 6 - len(team)))
        return team
    elif len(team) == 6 and not uncovered_types:
        return team
    else:
        create_team(_use_starter, _starter_pokemon, _useLegendaries, _pokedex, _types, _type_chart)


def successful_team(team):
    for mon in team:
        team[team.index(mon)] = mon.capitalize()
    print("Here's your team:")
    print("\n".join(team))
    print("Good luck out there!")

# ----------------------------- MAIN CODE -----------------------------

game, use_starter, starter_pokemon, useLegendaries, pokedex = user_choices()

types, type_chart = type_advantage_selection(game)

team = create_team(use_starter, starter_pokemon, useLegendaries, pokedex, types, type_chart)

while True:
    if type(team) == list:
        successful_team(team)
        break
    else:
        team = create_team(use_starter, starter_pokemon, useLegendaries, pokedex, types, type_chart)

