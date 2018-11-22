"""Code for parsing the backend of the Pokedex program
Starter code by David Szeto. Implementation by the CSCA20 student.
"""


import const


def get_pokemon_stats():
    """Reads the data contained in a pokemon data file and parses it into
    several data structures.

    Args:
        None

    Returns: a tuple of:
        -a dict where:
            -each key is a pokemon name (str)
            -each value is a tuple of the following stats:
                -pokemon name (str)
                -species_id (int)
                -height (float)
                -weight (float)
                -type_1 (str)
                -type_2 (str)
                -url_image (str)
                -generation_id (int)
                -evolves_from_species_id (str)
        -a dict where:
            -each key is a pokemon species_id (int)
            -each value is the corresponding pokemon name (str)
        -a list of all pokemon names (strs)
        -a dict where:
            -each key is a pokemon type (str). Note that type_1 and type_2
            entries are all considered types. There should be no special
            treatment for the type NA; it is considered a type as well.
            -each value is a list of all pokemon names (strs) that fall into
            the corresponding type
    """
    name_to_stats = {}
    id_to_name = {}
    names = []
    pokemon_by_type = {}

    # Write your code below.
    file = const.DATA_FILENAME
    reader = open(file, 'r+')
    # head = reader.readline().split(const.SEP)
    parsed_header = parse_header(reader)

    lines = reader.readlines()
    for line in lines:
        pokemon = line.strip().split(const.SEP)
        
        name = pokemon[parsed_header['pokemon']]
        species_id = pokemon[parsed_header['species_id']],
        
        type_1 = pokemon[parsed_header['type_1']]
        type_2 = pokemon[parsed_header['type_2']]
        name_to_stats[name] = (
            name,
            species_id[0],
            pokemon[parsed_header['height']],
            pokemon[parsed_header['weight']],
            type_1,
            type_2,
            pokemon[parsed_header['url_image']],
            pokemon[parsed_header['generation_id']],
            pokemon[parsed_header['evolves_from_species_id']],
        )
        id_to_name[int(species_id[0])] = name
        names.append(name)
        
        for t in [type_1, type_2]:
            if t not in pokemon_by_type:
                pokemon_by_type[t] = [name]
            else:
                pokemon_by_type[t].append(name)
    # Write your code above.
    return name_to_stats, id_to_name, names, pokemon_by_type


def parse_header(f):
    """Parses the header and builds a dict mapping column name to index

    Args:
        f: a freshly opened file in the format of pokemon.csv

    Returns:
        a dict where:
            -each key is one of:
                'pokemon', 'species_id', 'height', 'weight', 'type_1',
                'type_2', 'url_image', 'generation_id',
                'evolves_from_species_id'
            -each value is the index of the corresponding key in the CSV file
                starting from column 0.
                eg. If 'pokemon' is in the second column, then its index will
                be 1. If 'species_id' is the third column, then its index will
                be 2.
    """
    columns = ['pokemon', 'species_id', 'height', 'weight', 'type_1', 'type_2',
               'url_image', 'generation_id', 'evolves_from_species_id']
    result = {}

    # Write your code below.
    header = f.readline().split(const.SEP)
    for col in columns:
        result[col] = header.index(col)
    return result