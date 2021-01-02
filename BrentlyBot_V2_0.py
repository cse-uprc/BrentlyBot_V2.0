import discord
from discord.ext import commands
import json
from Util.UIService import serve_UI, log_message

client = commands.Bot(command_prefix="!")

with open("keys.json") as json_file:
    data = json.load(json_file)
    TOKEN = data["discordKey"]


@client.event
async def on_ready():
    # Display OLGA logging in
    log_message("Logged in as: {} - {}".format(client.user.name, client.user.id))
    log_message("Bot Comming online ...")
    # client.run(TOKEN)
serve_UI()
