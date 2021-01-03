from discord.ext import commands
import json
from Util.UIService import serve_UI, log_message
import Commands.officeHours as OfficeHours
import Commands.screenshot as Screenshot

client = commands.Bot(command_prefix="!")

with open("keys.json") as json_file:
    data = json.load(json_file)
    TOKEN = data["discordKey"]


@client.event
async def on_ready():
    # Display bot logging in
    log_message("Logged in as: {} - {}".format(client.user.name, client.user.id))
    log_message("Bot online")


@client.command()
async def screenshot(message, *args):
    await Screenshot.bot_screenshot(message, args)


@client.command()
async def officeHours(message, *args):
    await OfficeHours.bot_officeHours(message, args)

client.run(TOKEN)
# serve_UI()
