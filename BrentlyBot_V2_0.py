import discord
from discord.ext import commands
import random
import json
import sys
import pyautogui
from Util.UIService import serve_UI, log_message
import serverData

client = commands.Bot(command_prefix="!")
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("keys.json") as json_file:
    data = json.load(json_file)
    TOKEN = data["discordKey"]


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    # Take a screenshot
    if message.content.upper().startswith('!SCREENSHOT'):
        await message.channel.send('Your face!')

        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'screencapture.png')

        await message.channel.send(file=discord.File('screencapture.png'))

    log_message("Logged in as: {} - {}".format(client.user.name, client.user.id))
    log_message("Bot Comming online ...")
    # client.run(TOKEN)
serve_UI()

@client.event
async def on_raw_reaction_add(payload):
    print('event triggered')
    if payload.message_id != serverData.role_assignment_message_id:
        return

    try:
        role_id = serverData.emojiToRole[payload.emoji.name]
    except KeyError:
        print('Oof')
        return

    guild = client.get_guild(payload.guild_id)    
    if guild is None:
        return
        
    role = guild.get_role(role_id)
    if role is None:
        return
    
    try:
        await payload.member.add_roles(role)
        print('Role Assigned')
    except discord.HTTPException:
        pass

intents = discord.Intents.default()
intents.members = True
client.run(TOKEN)
