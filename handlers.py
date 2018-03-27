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
async def songs_api(request):
    songs = await Song.findAll(orderby='id desc')
    return {'songs': songs}

@get('/api/downloads/{title}')
async def download(request, *, title):

    path = '/Users/chenbin/Music/虾米音乐/' + title
    # 设置response
    response = aiohttp.web.StreamResponse(headers={'Content-Disposition': 'Attachment'})
    await response.prepare(request)
    with open(path, 'rb') as data:
        await response.write(data.read())
    return response

@get('/songs')
def songs():
    return {
        '__template__': 'songs.html'
    }
