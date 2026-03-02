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
from fastapi.staticfiles import StaticFiles




class SongDetails(BaseModel):
    ytlink:str
    curr_time:float
    song_ins:str

app=FastAPI()

@app.post('/fetchMPD')
async def startStreaming(data:SongDetails):
    obj=SongPlayer()
    # obj.create_manifest_for_songs()
    # obj.prepare_mpp_for_streaming()
    return StreamingResponse(obj.send_manifect_via_streaming(),media_type="application/dash+xml")



app.mount(
    "/music",
    StaticFiles(directory="/home/siddhant/Amuzeek/Amuzeek_Backend/src/songs"),
    name="songs"
)