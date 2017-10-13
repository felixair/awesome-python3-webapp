#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)
import orm, asyncio, os, json, time
from datetime import datetime
from models import User, Blog, Comment
from aiohttp import web

async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='123456789', image='about:blank')

    await u.save()
    

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()