import discord
from typing import Final
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# Helpers
from helpers.message_handler import on_message_handler
from helpers.ready_handler import on_ready_handler

with open('atepp/configs/telegram.json', 'r') as config_file:
    config = json.load(config_file)
TOKEN: Final = config['TOKEN']

@bot.event
async def on_ready():
    await on_ready_handler(bot)

@bot.event
async def on_message(message):
    await on_message_handler(bot, message)

bot.run(TOKEN)
