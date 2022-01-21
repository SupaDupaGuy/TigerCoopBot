import discord
import os
import sys
import asyncio
from replit import db
from keep_alive import keep_alive
from helperFunctions import *

# Global Variables
version = discord.__version__
client = discord.Client()
server = discord.Guild
helper = discord.utils


# Database Variables


@client.event
async def on_ready():
  print(f'Discord API Version {version}')
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # Variables
  msg = message.content

  # If the bot is the author, return
  if msg.author == client.user:
    return

  #


keep_alive()
client.run(os.getenv('TOKEN'))