#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, orm, asyncio
from datetime import datetime
from models import Song

pwd = "/Users/chenbin/Music/虾米音乐/"
print('      Size     Last Modified  Name')

for f in os.listdir(pwd):
        abspath = pwd + f
        fsize = os.path.getsize(abspath)
        mtime = datetime.fromtimestamp(os.path.getmtime(abspath)).strftime('%Y-%m-%d %H:%M')
        if fsize > 500:
            fsize = float(fsize) / 1024 / 1024
            print('%.2fM  %s  %s' % (fsize, mtime, f))

# async def insert_data(loop):
#     await orm.create_pool(loop, host='127.0.0.1', user='root', password='990978664', db='music')

#     for f in os.listdir(pwd):
#         abspath = pwd + f
#         fsize = os.path.getsize(abspath)
#         mtime = datetime.fromtimestamp(os.path.getmtime(abspath)).strftime('%Y-%m-%d %H:%M')
#         if fsize > 500:
#             fsize = float(fsize) / 1024 / 1024
#             print('%.2fM  %s  %s' % (fsize, mtime, f))
#             song = Song(path=abspath, title=f, date=mtime, size=fsize)
#             await song.save()
        

# loop = asyncio.get_event_loop()
# loop.run_until_complete(insert_data(loop))
                
