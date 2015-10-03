#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'zhangshen'

#test
import www.ORM
import asyncio

import time, uuid
from www.ORM import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(priamry_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(priamry_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    sumary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__= 'comments'

    id = StringField(priamry_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

def test(loop):
    yield from www.ORM.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')
    u= User(name='Test', email='test@example.com', passwd='12345678', image='about:blank')
    yield from u.save()

if __name__=='__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()