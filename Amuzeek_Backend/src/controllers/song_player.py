
from utils.common_functions.song_reader import return_song_list
from utils.common_functions.song_streamer import stream_songs
import ffmpeg
import subprocess


class SongPlayer:
    def __init__(self):
        self.song_list=return_song_list()
    
    def start_streaming(self):
        subprocess=subprocess.Popen( ["ffmpeg",
        "-i", "/home/siddhant/Amuzeek/Amuzeek_Backend/src/songs/moves_like_jagger.mp3",
        "-f", "wav",
        "pipe:1"
        ],
        stdout=subprocess.PIPE
        )
        while True:
            chunk=subprocess.stdout.read(1024)
            if not chunk:
                break
            yield chunk #This line essentially stores the state of the functional call stack , during intermediate function call and resumes the execution in next calls
            

