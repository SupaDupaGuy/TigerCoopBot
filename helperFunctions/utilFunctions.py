# Description
# Utility functions for modules command functions

class RoleList:
  roles = [None]
  

# Checks whether given message author has role in the moderator roles list
# Returns a boolean value
async def checkModRole(msg, modRoles):
  userRoles = msg.author.roles
  for role in modRoles:
    for userRole in userRoles:
      if userRole == role:
        return True
      
  return False


def sayHi():
  print("Hello User")