import discord
import os
import sys
import asyncio
from replit import db
from keep_alive import keep_alive
from helperFunctions.utilFunctions import *
from helperFunctions.initFunctions import *
from commands.mainCommands import *

# Global Variables
version = discord.__version__
client = discord.Client()
server = discord.Guild
helper = discord.utils

sayHi()
#moderatorRoles = RoleList()
#moderatorRoles.roles.append('Hi')
#moderatorRoles.roles.pop()
# Database Initialised Variables
#db["modRoles"] = moderatorRoles
#keys = db.keys()
#moderators = db["moderators"]

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

  # Commands
  userCommands(msg, bot_symbol)
  moderatorCommands(msg, bot_symbol, moderators)


keep_alive()
client.run(os.getenv('TOKEN'))