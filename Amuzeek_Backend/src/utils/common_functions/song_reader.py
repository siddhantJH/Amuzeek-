from pathlib import Path
folder=Path('/home/siddhant/Amuzeek/Amuzeek_Backend/songs')

song_list=[]

async def return_song_list():
    for files in folder.iter():
        song_list.append(files)
    return song_list