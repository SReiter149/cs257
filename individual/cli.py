"""
cli.py
Sam Reiter 4/17/2025
NAME: cli.py - command-line interface exercise
SYNOPSIS: python3 cli.py -a "album name"
DESCRIPTION: Shows a list of all the songs in the album, case sensitive
"""

import sys
import csv
import os
import pdb
import argparse

DIRECTORY = os.getcwd()

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description="Get the list of songs in the album")
    parser.add_argument("--album", "-a", help="name of album (case sensitive)", nargs = "+")
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def usage_statement():
    statement = f'Usage: {sys.argv[0]} "album name"\n'
    statement += 'returns the songs in the album'
    return statement

def getAlbum(album):
    songs = []
    with open('../data/songs.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["album"] == album:
                songs.append(row)
    return songs

def main():
    arguments = get_parsed_arguments()
    for album in arguments.album:
        songs = getAlbum(album)
        print(songs)

if __name__ == "__main__":
    main()
