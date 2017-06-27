import sqlite3


def setup_tracks(db, data_file):
    '''(str, file) -> NoneType
    Create and populate the Tracks table with
    the data from the open file data_file.'''

    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor

    cur = con.cursor()
    # Create the Tracks table
    cur.execute('CREATE TABLE Tracks ' +
                '(Title TEXT, ID INTEGER, Time INTEGER)')

    # Populate the Tracks Table
    # Loop through each line in the file:
    data_file.readline()
    for line in data_file:
        # get the data line by line and insert into the table
        data = line.split(',')

        title = data[0].strip()
        track_id = int(data[1].strip())

        time = data[2].strip()
        # split timestamp into min and second
        time_array = time.split(':')
        # convert min to second and sum them
        second = int(time_array[0]) * 60 + int(time_array[1])
        cur.execute('INSERT INTO Tracks VALUES ' +
                    '(?, ?, ?)', (title, track_id, second))

    # close the cursor
    cur.close()

    # commit the changes
    con.commit()

    # close the connection
    con.close()


def setup_genres(db, data_file):
    '''(str, file) -> NoneType
    Create and populate the Genres table with
    the data from the open file data_file.'''

    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor

    cur = con.cursor()
    # Create the Genres table
    cur.execute('CREATE TABLE Genres ' +
                '(Artist TEXT, Genres TEXT)')

    # Populate the Genres Table
    # Skip first line
    data_file.readline()
    # Loop through each line in the file:
    for line in data_file:
        # get the data line by line and insert into the table
        data = line.split(',')
        # data is [title, id, time] each is a str
        artist = data[0].strip()
        genres = data[1].strip()

        cur.execute('INSERT INTO Genres VALUES ' +
                    '(?, ?)', (artist, genres))

    # close the cursor
    cur.close()

    # commit the changes
    con.commit()

    # close the connection
    con.close()


def setup_albums(db, data_file):
    '''(str, file) -> NoneType
    Create and populate the Albums table with
    the data from the open file data_file.'''

    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor

    cur = con.cursor()
    # Create the Albums table
    cur.execute('CREATE TABLE Albums ' +
                '(ID INTEGER, Artist TEXT, Album TEXT)')

    # Populate the Albums Table
    # Skip first line
    data_file.readline()
    # Loop through each line in the file:
    for line in data_file:
        # get the data line by line and insert into the table
        data = line.split(',')
        # data is [id, artist, album] each is a str
        track_id = int(data[0].strip())
        artist = data[1].strip()
        album = data[2].strip()

        cur.execute('INSERT INTO Albums VALUES ' +
                    '(?, ?, ?)', (track_id, artist, album))

    # close the cursor
    cur.close()

    # commit the changes
    con.commit()

    # close the connection
    con.close()


def setup_popularity(db):
    '''(str) -> None
    The parameter is a database filename. Create and populate the
    Popularity table with the given database.
    '''
    # get all artist from Albums table
    query = 'SELECT DISTINCT(Artist) FROM Albums'
    artists = run_query(db, query)

    # connect to the database
    con = sqlite3.connect(db)
    # create a cursor

    cur = con.cursor()
    # Create the Popularity table
    cur.execute('CREATE TABLE Popularity ' +
                '(Artist TEXT, Hits INTEGER)')

    # Populate the Popularity Table
    # Loop through each line in the file:
    for artist_tuple in artists:
        # get the data line by line and insert into the table
        artist = artist_tuple[0]
        # insert artist with 0 hits
        cur.execute('INSERT INTO Popularity VALUES ' +
                    '(?, ?)', (artist, 0))

    # close the cursor
    cur.close()

    # commit the changes
    con.commit()

    # close the connection
    con.close()


def run_query(db, query, args=None):
    '''Return the results of running query q on database db.
    If given, args contains the query arguments.'''

    # create connection
    con = sqlite3.connect(db)
    # create cursor
    cur = con.cursor()
    # run the query
    # case when no args passed
    if args is None:
        cur.execute(query)
    else:
        # args has a value which should be a tuple
        cur.execute(query, args)

    # fetch result
    result = cur.fetchall()
    # close everything
    cur.close()
    con.close()
    return result


def run_command(db, query, args=None):
    '''Return the results of running query q on database db.
    If given, args contains the query arguments.'''

    # create connection
    con = sqlite3.connect(db)
    # create cursor
    cur = con.cursor()
    # run the query
    # case when no args passed
    if args is None:
        cur.execute(query)
    else:
        # args has a value which should be a tuple
        cur.execute(query, args)

    result = cur.fetchall()
    # commit result
    con.commit()
    # close everything
    cur.close()
    con.close()
    return result


def update_popularity(db, artist):
    '''(str, str) -> None
    Update the number of times the given artist/band has
    had a track searched for in the popularity table (add 1 to the hit value).
    '''
    # artist hits
    query = '''UPDATE Popularity SET Hits = Hits + 1
    WHERE Artist = ?'''
    run_command(db, query, (artist,))


def get_albums(db, artist):
    '''(str, str) -> list of tuple
    The first parameter is a database name and the second an artist or band's
    name. Return the unique album titles, track titles and ids produced by the
    artist/band.
    '''

    query = '''SELECT Albums.Album, Tracks.Title, Albums.ID FROM
    Albums JOIN Tracks ON Albums.ID = Tracks.ID WHERE Albums.Artist = ?'''
    return run_command(db, query, (artist,))


def get_greatest(db):
    '''(str) -> list of tuple
    The parameter is a database name. Return a list of tuples containing
    all those unique artist names whose albums have the word 'Greatest' in
    their title.
    '''

    query = '''SELECT * FROM Albums WHERE Album LIKE ? GROUP BY artist'''
    return run_command(db, query, ('%Greatest%',))


def get_genres(db, album):
    '''(str, str) -> list of tuple
    The first parameter is a database name, the second is an album.  Return
    the artists that produced the album and the genres associated with that
    artist. It's possible for more than one artist to have the same album title
    and for an artist to belong to more than one genres.
    '''

    query = '''SELECT DISTINCT Genres.Artist, Genres.Genres FROM Albums JOIN Genres
    ON Albums.Artist = Genres.Artist WHERE Albums.Album = ?'''
    return run_command(db, query, (album,))


def get_track_info(db, title):
    '''(str, int) -> list of tuple
    The first parameter is a database name and the second is a track title.
    Return the track's title, ID, band/artist, album name and time. This
    function should update the popularity table by adding 1 to the
    Hits field of the corresponding artist/band.
    '''
    query = '''SELECT Tracks.Title, Tracks.ID, Albums.Artist, Albums.Album,
    Tracks.Time FROM Tracks JOIN Albums ON Tracks.ID = Albums.ID
    WHERE Tracks.Title = ?'''
    results = run_command(db, query, (title,))
    for result in results:
        artist = result[2]
        # update artist popularity
        update_popularity(db, artist)
    return results


def get_album_lengths(db):
    '''(str) -> list of tuples
    The parameter is a database name. Return a list of tuples
    containing each artist name, album title and total length
    of the album.
    '''
    query = '''SELECT Albums.artist, Albums.Album, SUM(Tracks.Time)
    FROM Albums JOIN Tracks ON Albums.ID = Tracks.ID GROUP BY Albums.Album'''
    return run_query(db, query)


def multiple_albums(db):
    '''(str) -> list of tuple
    The parameter is a database name. Return a list of tuples of artists
    with more than one album.
    '''
    query = 'SELECT artist FROM Albums GROUP BY Album HAVING COUNT(Album) > 1'
    return run_query(db, query)


def get_dict_of_artists(db, artist_list):
    '''(str, list of tuple) -> dict of dict
    Given a database name and a list of tuples containing artist/band
    names (for example [('The Beatles',), ('The Tragically Hip', )]).
    Return a dictionary whose keys are artist/band names and
    values are dictionaries with key equal to album title and values
    a list of track titles (ie, a list of str not a list of tup).
    '''
    # new dictionary
    artist_dict = {}
    for artist_tuple in artist_list:
        artist = artist_tuple[0]
        # add artist as key and create empty dictionary as value
        artist_dict[artist] = {}
        # get albums infomation with artist
        albums = get_albums(db, artist)
        for album_tuple in albums:
            album = album_tuple[0]
            track = album_tuple[1]
            # if album is already the key, append track to value
            if album in artist_dict[artist]:
                artist_dict[artist][album].append(track)
            else:
                # add album as key, track list as value
                artist_dict[artist][album] = [track]
    return artist_dict


def get_num_Albums(db):
    '''(str) -> list of tuple
    GIven a database, return a list of tuples of the artist
    names and number of Albums produced by that artist
    '''
    query = 'SELECT Artist, COUNT(ALBUM) FROM Albums GROUP BY Artist'
    return run_query(db, query)


def get_popularity(db):
    '''(str) -> list of tuple
    Return the artists and hits from the popularity table.
    '''
    return run_query(db, '''SELECT Artist, Hits FROM Popularity''')
