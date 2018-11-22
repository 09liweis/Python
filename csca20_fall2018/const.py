"""Some constants for use with the Pokedex program
Starter code by David Szeto. Implementation by the CSCA20 student.
"""

# Reading the data ------------------------------------------------------------
DATA_FILENAME = 'pokemon.csv'  # The filename of the CSV we'll be reading
SEP = ','  # The separator of the values in the CSV

# Handling images -------------------------------------------------------------
SHOW_IMAGES = True  # Whether or not to show images of pokemon to user
IMAGES_DIR = './images/'  # The directory we're storing our images in; will only
# be used if SHOW_IMAGES is set to True