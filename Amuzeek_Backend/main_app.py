"""
Main purpose of this script is to start an api which basically streams the music or song to the endpoint 
which asks for the song
"""

import fastapi
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import os

app=FastAPI()
music_path='../songs'


@app.post('/streamSong')
def startStreaming():
    return {"Hello":"siddhant"}
