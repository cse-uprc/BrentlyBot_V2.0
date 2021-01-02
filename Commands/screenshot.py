import discord
import pyautogui
from Util.UIService import log_message

# --------------------------------------------------
# Takes screenshot of Instructors screen
#
# @param message - reference to channel information
# @param args - parameters passed with command
# @return none
# --------------------------------------------------
async def bot_screenshot(message):
    log_message("Taking Screenshot ...")
    await message.channel.send('Your face!')

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screencapture.png')

    await message.channel.send(file=discord.File('screencapture.png'))
