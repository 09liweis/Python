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
    sep = ','
    allData = []
    with open(const.DATA_FILENAME, newline='') as myData:
        for line in myData:
            line = line.strip()
            line = line.split(sep)
            allData.append(line)
    order = parse_header(myData)
    species_id = order['species_id']
    evolves_from_species_id = order['evolves_from_species_id']
    height = order['height']
    weight = order['weight']
    type_1 = order['type_1']
    url_image = order['url_image']
    pokemon = order['pokemon']
    type_2 = order['type_2']
    generation_id = order['generation_id']
    i = 1
    name_to_stats = {}
    id_to_name = {}
    names = []
    pokemon_by_type = {}
    while i < len(allData):
        curr = allData[i]
        name_to_stats[curr[pokemon]] = (curr[pokemon], int(curr[species_id]),
                                        float(curr[height]),
                                        float(curr[weight]),
                                        curr[type_1], curr[type_2],
                                        curr[url_image],
                                        int(curr[generation_id]),
                                        curr[evolves_from_species_id])
        id_to_name[int(curr[species_id])] = curr[pokemon]
        names.append(curr[pokemon])
        if pokemon_by_type.get(curr[type_1]) is None:
            pokemon_by_type[curr[type_1]] = []
        if pokemon_by_type.get(curr[type_2]) is None:
            pokemon_by_type[curr[type_2]] = []
        pokemon_by_type[curr[type_1]].append(curr[pokemon])
        pokemon_by_type[curr[type_2]].append(curr[pokemon])
        i += 1
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
    sep = ','
    result = {}
    allData = []
    with open(const.DATA_FILENAME, newline="") as myData:
        for line in myData:
            line = line.strip()
            line = line.split(sep)
            allData.append(line)
    for i in columns:
        j = 0
        while j < len(allData[0]):
            if allData[0][j] == i:
                result[i] = j
            j += 1
    return result