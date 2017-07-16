#!/usr/bin/env python3
import json

import aiohttp
from aiotg import Bot, Chat

from config import TG_TOKEN

bot = Bot(api_token=TG_TOKEN)


@bot.command(r"ping")
def ping(chat: Chat, match):
    return chat.reply('pong')


@bot.command(r"/start")
def start(chat: Chat, match):
    return chat.send_text('ask me something')


@bot.command(r".*")
async def answer(chat: Chat, match):
    async with http_client_session.get('http://api.duckduckgo.com/?q={}&format=json'.format(
            match.group(0)
    )) as resp:
        result_text = await resp.text()
        result_json = json.loads(result_text)
        await chat.send_text(result_json['AbstractText'])


if __name__ == "__main__":
    http_client_session = aiohttp.ClientSession()
    bot.run()
