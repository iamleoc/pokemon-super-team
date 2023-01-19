# Different games have different types available to them, and have different relationships with each other.
# It's important to keep all types in all twice_as_effective dicts, as the pokedexes include all a pokemon's types, so steel and fairy are included in gen 1

gen1_types = {"normal", "flying", "fighting", "poison", "ground", "rock", "bug", "ghost", "fire", "water", "grass", "electric", "psychic", "ice", "dragon"}

gen1_twice_as_effective = {
    "normal": [],
    "fighting": ["normal", "rock", "ice"],
    "flying": ["fighting", "bug", "grass"],
    "poison": ["bug", "grass"],
    "ground": ["poison", "rock", "fire", "electric"],
    "rock": ["flying", "bug", "fire", "ice"],
    "bug": ["poison", "grass", "psychic"],
    "ghost": ["ghost"],
    "fire": ["bug", "grass", "ice"],
    "water": ["ground", "rock", "fire"],
    "grass": ["ground", "rock", "water"],
    "electric": ["flying", "water"],
    "psychic": ["fighting", "poison"],
    "ice": ["flying", "ground", "grass", "dragon"],
    "dragon": ["dragon"],
    "steel": [],
    "dark" : [],
    "fairy": [],
}

gen2to5_types = {"normal", "flying", "fighting", "poison", "ground", "rock", "bug", "ghost", "fire", "water", "grass", "electric", "psychic", "ice", "dragon", "dark", "steel"}

gen2to5_twice_as_effective = {
    "normal": [],
    "fighting": ["normal", "rock", "ice", "steel", "dark"],
    "flying": ["fighting", "bug", "grass"],
    "poison": ["poison", "grass"],
    "ground": ["poison", "rock", "fire", "electric", "steel"],
    "rock": ["flying", "bug", "fire", "ice"],
    "bug": ["grass", "psychic", "dark"],
    "ghost": ["ghost", "psychic"],
    "fire": ["bug", "grass", "ice", "steel"],
    "water": ["ground", "rock", "fire"],
    "grass": ["ground", "rock", "water"],
    "electric": ["flying", "water"],
    "psychic": ["fighting", "poison"],
    "ice": ["flying", "ground", "grass", "dragon"],
    "dragon": ["dragon"],
    "steel": ["rock", "ice"],
    "dark": ["ghost", "psychic"],
    "fairy": [],
}

gen6on_types = {"normal", "flying", "fighting", "poison", "ground", "rock", "bug", "ghost", "fire", "water", "grass", "electric", "psychic", "ice", "dragon", "dark", "steel", "fairy"}

gen6on_twice_as_effective = {
    "normal": [],
    "fighting": ["normal", "rock", "ice", "steel", "dark"],
    "flying": ["fighting", "bug", "grass"],
    "poison": ["poison", "grass", "fairy"],
    "ground": ["poison", "rock", "fire", "electric", "steel"],
    "rock": ["flying", "bug", "fire", "ice"],
    "bug": ["grass", "psychic", "dark"],
    "ghost": ["ghost", "psychic"],
    "fire": ["bug", "grass", "ice", "steel"],
    "water": ["ground", "rock", "fire"],
    "grass": ["ground", "rock", "water"],
    "electric": ["flying", "water"],
    "psychic": ["fighting", "poison"],
    "ice": ["flying", "ground", "grass", "dragon"],
    "dragon": ["dragon"],
    "steel": ["rock", "ice", "fairy"],
    "dark": ["ghost", "psychic"],
    "fairy": ["fighting", "dragon", "dark"],
}
