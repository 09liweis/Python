"""The frontend and logic of the Pokedex program.
Starter code by David Szeto. Implementation by the CSCA20 student.
"""


import math

import backend
import const


# The following code will only run if you set const.SHOW_IMAGES to True.
# DON'T MODIFY THE CODE IN THE SECTION BELOW ----------------------------------
if const.SHOW_IMAGES:
    # In case you're curious, this block of code attempts to import matplotlib.
    # If it succeeds, good!
    # If it fails, then it uses a Python tool named PIP to install the missing
    # modules into your Python library, and then again imports matplotlib
    try:
        from matplotlib import pyplot as plt
        from matplotlib import image as mpimg
    except ModuleNotFoundError:
        print('You didn\'t have matplotlib installed but you set '
              'const.SHOW_IMAGES to True. Attempting to automatically '
              'install...')
        # This try-except statement handles the case where different versions
        # of pip provide different functions to call
        try:
            from pip import main as pipmain
        except:
            from pip._internal import main as pipmain
        # The following line installs matplotlib
        pipmain(['install', 'matplotlib'])
        from matplotlib import pyplot as plt
        from matplotlib import image as mpimg
        print('Installation successful')
# DON'T MODIFY THE CODE IN THE SECTION ABOVE ----------------------------------


def main():
    """The main function of the Pokedex program.

    Args:
        None

    Returns:
        None
    """
    stats, id_to_name, names, pokemon_by_type = backend.get_pokemon_stats()
    
    # Write your code below.
    choice = get_main_choice()
    while choice != '0':
        if choice == '1':
            name = find_pokemon_by_name(names)
            display_stats(stats[name])
        if choice == '2':
            name = find_pokemon_by_id(id_to_name)
            print(stats[name])
            display_stats(stats[name])
        if choice == '3':
            name = display_pokemon_by_type(pokemon_by_type)
        choice = get_main_choice()
    print('Goodbye!')


def get_main_choice():
    """Asks the user for a choice of how they'd like to use the pokedex.

    If the user enters an invalid choice, repeatedly prompts them until they
    enter a correct one.

    Args:
        None

    Returns:
        The user's choice as a str, which can be '0', '1', '2', or '3'
    """
    # This is the prompt you'll display to the user to ask for their choice.
    # Don't modify it!
    prompt = ('Choose an option (0 - 3):\n'
              '0: quit program\n'
              '1: find pokemon by name\n'
              '2: find pokemon by number\n'
              '3: list pokemon by type\n')
    # This is the prompt you'll display to the user if they enter something
    # invalid. Don't modify it!
    warning = 'Invalid choice. Please try again.'

    # Write your code below.
    choice = input(prompt)
    while choice not in ['0', '1', '2', '3']:
        print(warning)
        choice = input(prompt)
    return choice


def find_pokemon_by_name(pokemon_names):
    """Asks the user for a pokemon name for which they'd like the stats.

    Implicitly converts the name entered by the user to lower case.

    If the user enters a name of a pokemon which is not in pokemon_names, asks
    the user if they meant <name>, where <name> is the most similar pokemon
    name in pokemon_names according to the Levenshtein distance. Then, repeats
    until the user enters a valid pokemon name

    Args:
        pokemon_names: a list of all of the names of pokemon (strs)

    Returns:
        The pokemon name chosen by the user (as a str)
    """
    # This is the prompt you'll display to the user to ask for their choice.
    # Don't modify it!
    prompt = 'Enter the name of a pokemon: '
    # This is the prompt you'll display to the user if they enter something
    # invalid. Don't modify it! However, you'll be required to fill in the
    # placeholders with the appropriate values.
    warning = 'I don\'t recognize the name {0}. Did you mean {1}?'

    # Hint: use the find_closest_word() function to help you out here.

    # Write your code below.
    search = input(prompt).lower()
    while search not in pokemon_names:
        name = find_closest_word(search, pokemon_names)
        print(warning.format(search, name))
        search = input(prompt)
    return search


def find_closest_word(word_0, words):
    """Finds the closest word in the list to word_0 as measured by the
    Levenshtein distance

    Args:
        word_0: a str
        words: a list of str

    Returns:
        The closest word in words to word_0 as a str.
    """
    # Hint: use the levenshtein_distance() function to help you out here.

    # Write your code below.
    closest_word = ''
    first_dis = levenshtein_distance(word_0, words[0])
    print(first_dis)
    for word in words:
        distance = levenshtein_distance(word_0, word)
        if distance <= first_dis:
            first_dis = distance
            closest_word = word
    return closest_word


def levenshtein_distance(s1, s2):
    """Returns the Levenshtein distance between strs s1 and s2

    Args:
        s1: a str
        s2: a str
    """
    # This function has already been implemented for you.
    # Source of the implementation:
    # https://stackoverflow.com/questions/2460177/edit-distance-in-python
    # If you'd like to know more about this algorithm, you can study it in
    # CSCC73 Algorithms. It applies an advanced technique called dynamic
    # programming.
    # For more information:
    # https://en.wikipedia.org/wiki/Levenshtein_distance
    # https://en.wikipedia.org/wiki/Dynamic_programming
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1],
                                           distances_[-1])))
        distances = distances_
    return distances[-1]


def find_pokemon_by_id(id_to_name):
    """Asks the user for a pokemon number for which they'd like the stats.

    If the user enters something invalid (ie. anything that's not a valid
    number of a pokemon), warns the user and repeats until they enter a valid
    pokemon number.

    Args:
        id_to_name: a dict mapping pokemon species_id (ie. pokemon number as an
        int) to pokemon name (as a str). It is assumed that the species ids are
        contiguous numbers starting from 1; eg. if there are 721 pokemon, then
        the species_id values will be the numbers from 1 to 721 (inclusive)

    Returns:
        The name of the pokemon chosen by the user (as a str).
    """
    max_pokemon_id = int(max(id_to_name))
    # This is the prompt you'll display to the user to ask for their choice.
    # Don't modify it!
    prompt = 'Enter a pokemon number (1 - {0}): '.format(max_pokemon_id)
    # This is the prompt you'll display to the user if they enter something
    # invalid. Don't modify it! However, you'll be required to fill in the
    # placeholders with the appropriate values.
    warning = 'Please enter a number between 1 and {0}'.format(max_pokemon_id)

    # Hint: the user chooses an id, but you need to return the name of the
    # pokemon with that id.

    # Write your code below.
    pokemon_id = int(input(prompt))
    while pokemon_id > max_pokemon_id:
        print(warning)
        pokemon_id = int(input(prompt))
    name = id_to_name[pokemon_id]
    return name


def display_stats(stats):
    """Prints the stats of a pokemon to the user.

    If const.SHOW_IMAGES is set to True, displays the image of the pokemon to
    the user.

    Args:
        stats: a tuple of:
            -pokemon name (str)
            -species_id (int)
            -height (float)
            -weight (float)
            -type_1 (str)
            -type_2 (str)
            -url_image (str)
            -generation_id (int)
            -evolves_from_species_id (str)

    Returns:
        None
    """
    # This function has already been implemented for you. You don't need to do
    # anything with it except call it in the appropriate location!
    template = ('Pokemon name: {0}\n'
                'Pokemon number: {1}\n'
                'Height (in m): {2}\n'
                'Weight (in kg): {3}\n'
                'Type 1: {4}\n'
                'Type 2: {5}\n'
                'Generation: {6}\n'
                'Evolves from: {7}\n')
    text = template.format(stats[0], stats[1], stats[2], stats[3], stats[4],
                           stats[5], stats[7], stats[8])
    print(text, end='')
    if const.SHOW_IMAGES:
        img_filename = stats[6]
        if img_filename.endswith('.png'):
            image = mpimg.imread(const.IMAGES_DIR + img_filename)
            plt.clf()
            plt.imshow(image)
            plt.show()
        else:
            print('No image for this Pokemon available')


def display_pokemon_by_type(pokemon_by_type):
    """Asks the user for a type of pokemon and displays the names of all
    pokemon with that type.

    If the user enters an invalid type, warns the user and repeats until they
    enter a valid one.

    Args:
        pokemon_by_type: a dict where:
            -each key is a pokemon type (str)
            -each value is a list of all pokemon (strs) with the given type

    Returns:
        None
    """
    pokemon_types = list(pokemon_by_type.keys())
    # This is the prompt you'll display to the user to ask for their choice.
    # Don't modify it!
    prompt = ('enter a type from one of the following: {0}\n'.format(
        ', '.join(pokemon_types)))
    # This is the prompt you'll display to the user if they enter something
    # invalid. Don't modify it!
    warning = 'Unrecognized type'

    # Write your code below.
    pokemon_type = input(prompt)
    while pokemon_type.lower() not in pokemon_types:
        print(warning)
        pokemon_type = input(prompt)
    pokemons = pokemon_by_type[pokemon_type]
    print('\n'.join(pokemons))


if __name__ == '__main__':
    main()