from music import *

import webbrowser
import os


def display_dict_in_browser(d):
    '''(dict) -> None
    Display the given dictionary in a browser.
    '''
    path = os.getcwd()

    table = '<table><tr>'
    table += '</tr>\n'
    for (key, value) in d.items():
        table += "<tr><td><strong>" + key + '</strong></td></tr>'
        for album in value.keys():
            table += '<tr><td></td><td><font color="blue" >' + album.upper() + '</font><br></td></tr>'
            for track in value[album]:
                table += '<tr><td></td><td>' + track+'</td></tr>'
        table += '\n'
    table += '</table>'

    output = open("results_dict.html", "w")
    output.write(table)
    output.close()

    webbrowser.open("file:///"+path+"/results_dict.html")

    return None


def display_table_in_browser(header, results):
    '''(list of str, list of tuple) -> None
    Display the list of tuples in an html table.
    '''
    table = '<table><tr>'
    for item in header:
        table += '<th>' + str(item) + '</th>'
    table += '</tr>\n'
    for tup in results:
        table += '<tr>'
        for item in tup:
            table += '<td>' + str(item) + '</td>'
        table += '</tr>\n'
    table += '</table>'

    path = os.getcwd()
    output = open("results.html", "w")
    output.write(table)
    output.close()

    webbrowser.open("file:///"+path+"/results.html")

    return None


if __name__ == '__main__':

    db = 'music.db'
    setup = False

    if setup:
        reader = open('albums.csv', 'r')
        setup_albums(db, reader)
        reader.close()
        reader = open('tracks.csv', 'r')
        setup_tracks(db, reader)
        reader.close()
        reader = open('genres.csv', 'r')
        setup_genres(db, reader)
        reader.close()
        setup_popularity(db)
    display_table_in_browser(['Albums', 'Tracks', 'ID'], get_albums(db, 'The Tragically Hip'))
