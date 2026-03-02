
from utils.common_functions.song_reader import return_song_list
from utils.common_functions.song_streamer import stream_songs
import ffmpeg
import subprocess
import time
import asyncio

global global_streamer_checkpoints

class SongPlayer:
    def __init__(self):
        self.song_list=return_song_list()
        self.listener_checkpoints=None

    def equalise_content_time(self):
         self.listener_checkpoints=global_streamer_checkpoints

    def create_manifest_for_songs(self):
        sub=subprocess.Popen( ["ffmpeg",
        "-i", "/home/siddhant/Amuzeek/Amuzeek_Backend/src/songs/moves_like_jagger.mp3",
        "-map","0:a","-c:a","aac","-seg_duration","4","-f","dash","/home/siddhant/Amuzeek/Amuzeek_Backend/src/songs/moves_like_jagger_manifest.mpd"
        ]
        )
        sub.run()
    
    async def send_manifect_via_streaming(self):
        from pathlib import Path
        chunksize=1024
        with open('/home/siddhant/Amuzeek/Amuzeek_Backend/src/songs/moves_like_jagger_manifest.mpd','r') as f:
            while True:
                content=f.read(chunksize)
                if not content:
                    break

                yield content


        
        





# ffmpeg -i moves_like_jagger.mp3 \
# -map 0:a \
# -c:a aac \
# -seg_duration 4 \
# -f dash \
# moves_like_jagger_manifest.mpd