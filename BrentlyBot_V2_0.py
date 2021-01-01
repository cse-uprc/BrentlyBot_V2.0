import discord
from discord.ext import commands
import json

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

client.run(TOKEN)