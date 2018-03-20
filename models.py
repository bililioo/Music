#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from orm import Model, StringField, BooleanField, FloatField, TextField

class Song(Model):
    __table__ = 'songs'

    title = StringField(ddl='varchar(500)')
    path = StringField(ddl='varchar(500)')
    size = StringField(ddl='varchar(500)')
    date = StringField(ddl='varchar(500)')
    id = StringField(primary_key=True ,ddl='int(11)')
