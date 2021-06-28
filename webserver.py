import logging
from flask import Flask
from threading import Thread
import asyncio
from discord.ext import tasks
#from counts import counts
from aiohttp import ClientSession as cs

#Count = counts()
app = Flask('')
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def home():
	return "I'm alive"


def run():
	app.run(host='0.0.0.0', port=4444)


async def _uptime():
	async with cs() as s:
		await s.get("https://danbot-uptime.zaeem20.repl.co")
		await s.close()
	#Count.add("web", Count.Len["web"] + 1)


def keep_alive():
	t = Thread(target=run)
	#uptimer.start()
	t.start()
	