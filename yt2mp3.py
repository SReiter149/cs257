# importing packages 
from pytube import YouTube, Playlist
import os 

os.chdir("/Users/sam/Library/Mobile Documents/com~apple~CloudDocs/Documents/Personal/Albums")

def getSongs():
    # INPUTS!! CHANGE EACH TIME
    p = Playlist("https://www.youtube.com/playlist?list=PLDhajrZgo0TLtVVg0twVHglQnrd-p38Sc")
    Album_Name = "Stick Season"
    destination = "/Users/sam/Library/Mobile Documents/com~apple~CloudDocs/Documents/Personal/Albums/" + Album_Name

    # Trim unwanted videos
    videos = list(p.video_urls)
    # Remember to remove
    # del videos[22]

    for url in videos:
        # get numbers
        number = videos.index(url) + 1
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first() 
        
        # download the file 
        out_file = video.download(output_path=destination) 

        # save the file/rename
        base, ext = os.path.splitext(out_file) 
        name = base.split("/")
        name[-1] = "(" + str(number) + ")" + name[-1]
        print(name[-1])
        base = "/".join(name)
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 

def playSongs(song):
    """
    Play the music using ffplay
    """
    os.system("ffplay " + song)

getSongs()