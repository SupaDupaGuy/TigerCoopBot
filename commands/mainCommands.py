from ..helperFunctions import utilFunctions as util
from ..main import bot_symbol

commandList = (
  "Here are a list of commands: \n" +
  f"Format  | {bot_symbol}[command] [expected data] | Explaination\n" +
  f"{bot_symbol}help   | Sends a list of commnads to the user in a DM.\n" +
  f"{bot_symbol}hello  | Says hello to the user."
)
modCommandList = (
  "Here are a list of Moderator commands: \n" +
  f"Format | {bot_symbol}[command] [expected data] | Explaination\n" +
  f"{bot_symbol}$addModRole [Role Name] | Gives the role access to bot mod commands"
)
ownerCommandsList = (
  "Here are a list of Owner commands: \n" +
  f"Format | {bot_symbol}[command] [expected data] | Explaination\n" +
  f"{bot_symbol}addModRole [Role Name] | Gives the role access to bot mod commands\n" +
  f"{bot_symbol}removeModRole [Role Name] | Removes the role's access to bot mod commands\n" +
  f"{bot_symbol}listModRoles | Lists the roles that have access to the bot mod commands.\n" +
  f"{bot_symbol}addWaitingRoom [Channel Name] | Lists and treats the given channel as a waiting room.\n" +
  f"{bot_symbol}removeWaitingRoom [Channel Name] | The given channel will no longer be treated like a waiting room\n" +
  f"{bot_symbol}listWaitingRooms | Lists all of the channels treated as a Waiting Room\n"
)


def userCommands(msg, bot_symbol):
  if msg.startswith(f"{bot_symbol}help"):
    await msg.channel.send("commandsList")
    return
  

def moderatorCommands(msg, bot_symbol, modRoles):
  if await util.checkModRole(msg, modRoles) or msg.author.id == msg.guild.owner.id:
    # Call Mod Commands
    print(" ")

  
