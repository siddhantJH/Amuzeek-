"""
Main purpose of this script is to start an api which basically streams the music or song to the endpoint 
which asks for the song
"""

import fastapi
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import os
from controllers.song_player import SongPlayer
from fastapi.responses import StreamingResponse
from pydantic import BaseModel



class SongDetails(BaseModel):
    ytlink:str
    curr_time:float
    song_ins:str

app=FastAPI()

@app.post('/streamSong')
def startStreaming(data:SongDetails):
    print("data--->",data)
    song_bytes=[]
    return StreamingResponse([SongPlayer().start_streaming()],media_type='audio/wav')
