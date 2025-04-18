"""
cli.py
NAME: cli.py - command-line interface exercise
SYNOPSIS: python3 cli.py "album name"
DESCRIPTION: Shows a list of all the songs in the album, case sensitive
"""


import sys
import pandas as pd
import os
import pdb

DIRECTORY = os.getcwd()

def usage_statement():
    statement = f'Usage: {sys.argv[0]} "album name"\n'
    statement += 'returns the songs in the album'
    return statement

def readcsv():
    songs = pd.read_csv("../data/songs.csv")
    return songs

def getAlbum(songs):
    albumSearch = sys.argv[1]
    if albumSearch in set(songs["album"].to_list()):
        albumSongs = songs[songs["album"] == albumSearch]["title"].to_list()
    else:
        return "album not found, try a new album name"
    # pdb.set_trace()
    return albumSongs


if __name__ == "__main__":
    songs = readcsv()
    print(getAlbum(songs))

