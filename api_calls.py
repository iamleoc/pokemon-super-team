import requests

"""
This code is not used in the main running of the Team Builder. This code simply helps build the dictionaries that are
used for the Pokedexes in pokedexes.py, by using PokeAPI.co.
"""

pokemon_endpoint = "https://pokeapi.co/api/v2/pokedex/29"
response = requests.get(url=pokemon_endpoint)
data = response.json()
pokemon = data["pokemon_entries"]

pokedex = {}

names = []

for pokemon in pokemon:
    names.append(pokemon["pokemon_species"]["name"])

for poke_name in names:
    print(poke_name)
    # This print line can be helpful in identifying which pokemon's name causes an error on the next line,
    # as some Pokemon show up with the variations in the PokeAPI call e.g. Wormadam is wormadam-plant.
    # These variations can sometimes have different types, so it's important to identify them all.
    # To help find the names for PokeAPI, search with their Pokedex # in 'v2/pokemon-species/dexnumber'
    name_response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{poke_name}")
    poke_data = name_response.json()
    types_list = []
    for t in poke_data["types"]:
        poke_type = t["type"]["name"]
        types_list.append(poke_type)
    pokedex[poke_name] = types_list

print(pokedex)
