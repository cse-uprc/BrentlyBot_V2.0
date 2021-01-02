import discord
import pyautogui
import json
from Util.UIService import log_message

async def bot_screenshot(message, *args):
    # Take a screenshot
    await message.channel.send('Your face!')

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screencapture.png')

    await message.channel.send(file=discord.File('screencapture.png'))


async def bot_officeHours(message, *args):
    messageUser = "{}#{}".format(message.author.name, message.author.discriminator)
    params = [x.upper() for x in list(filter(None, args[0]))]

    file = open("officeHours.json", "r")
    data = json.load(file)
    teacher = {}

    try:
        teacher = data['TEACHERS'][messageUser.upper()]
    except:
        log_message("{} does not have access to modify office hours".format(messageUser))

    print(params)
    print("-----------------------------")
    print(teacher)

    if params[0] == '-ADD':
        teacher[params[1]] = {"START": params[2], "END": params[3]}
    elif params[0] == '-EDIT':
        # Make your edits to the file here.
        teacher[params[1]]["START"] = params[2]
        teacher[params[1]]["END"] = params[3]
    elif params[0] == '-DELETE':
        # Delete the entered day here.
        teacher.pop(params[1], None)
        #teacher[params[1]] = None
    elif params[0] == '-NEWTEACHER':
        if(messageUser in data["ADMINS"]):
            data["TEACHERS"][params[1]] = {}
        else:
            log_message("{} user can not create new teachers. Insufficent Permissions".format(message.author))

    file.close()
    file = open("officeHours.json", "w")
    json.dump(data, file)
