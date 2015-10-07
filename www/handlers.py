__author__ = 'zhangshen'

' url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from www.coroweb import get, post
from www.models import User, Blog, Comment, next_id

@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs =[
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blog.html',
        'blogs': blogs
    }

@get('/api/users')
def api_get_users():
    users=User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)