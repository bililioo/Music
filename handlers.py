#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' url handlers '

from models import Song
from apis import APIValueError, APIResourceNotFoundError
from coroweb import get, post
from config import configs
from aiohttp import web
import aiohttp

@get('/api/songs')
async def songs_api():
    songs = await Song.findAll(orderby='id desc')
    return {'songs': songs}

@post('/api/songs')
def download_song(path):
    # if not title:
    #     raise APIValueError('title', 'Invalid title.')
    if not path:
        raise APIValueError('path', 'Invalid path.')
    
    response = aiohttp.web.StreamResponse()
    fn = open(path)
    response.body = fn
    # response.content_type = 'application/'
    return response


@get('/api/tempdownload')
async def download():
    path = '/Users/kkucars/Music/虾米音乐/阿细-追光者 (粤语).mp3'

    # response = aiohttp.web.StreamResponse()
    response = aiohttp.web.StreamResponse(headers={'Content-Disposition': 'Attachment'})
    # response.prepare()
    with open(path, 'r') as data:
        await response.write(data)
    return response

@get('/songs')
def songs():
    return {
        '__template__': 'songs.html'
    }

    