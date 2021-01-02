import discord
from discord.ext import commands
import random
import json
import sys
import pyautogui

client = commands.Bot(command_prefix = "!")

with open("keys.json") as json_file:
    data = json.load(json_file)
    TOKEN = data["discordKey"]

@client.event
async def on_ready():
    # Display OLGA logging in
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

client.run(TOKEN)