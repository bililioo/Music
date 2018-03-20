#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' url handlers '

from models import Song
import apis
from coroweb import get, post
from config import configs
from aiohttp import web

@get('/api/songs')
async def songs_api():
    songs = await Song.findAll(orderby='id desc')
    return {'songs': songs}


@get('/songs')
def songs():
    return {
        '__template__': 'songs.html'
    }