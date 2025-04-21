'''
    api.py
    Jeff Ondich, 22 April 2016
    Sam Reiter, 4/20/2025
    Last updated 20 April 2025
'''

import sys
import argparse
import flask
import json
import csv

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from the world of music'

@app.route('/temp')
def temp():
    return "yay!"

@app.route("/album/<albumName>")
def getAlbum(albumName):
    songs = {}
    with open('../data/songs.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["album"].lower() == albumName.lower():
                songs[len(songs.keys()) + 1] = row['title']
    return json.dumps(songs)

@app.route('/help')
def get_help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)