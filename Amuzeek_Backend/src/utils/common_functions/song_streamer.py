import ffmpeg

def stream_songs(song_path):
    audio=ffmpeg.input(song_path)
    out=audio.output(song_path)  
    return out