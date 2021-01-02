import json
import discord
import datetime
from Util.UIService import log_message

# --------------------------------------------------
# Command the processes officeHours command
#
# @Command !officeHours -<TYPE>
#
# @param message - reference to channel information
# @param args - parameters passed with command
# @return none
# --------------------------------------------------


async def bot_officeHours(message, *args):
    messageUser = "{}#{}".format(
        message.author.name, message.author.discriminator)
    params = [x.upper() for x in list(filter(None, args[0]))]

    file = open("officeHours.json", "r")
    data = json.load(file)
    methods = {"-ADD": office_hours_add,
               "-EDIT": office_hours_edit,
               "-DELETE": office_hours_delete,
               "-LIST": office_hours_list
               }

    if(is_teacher(data, messageUser)):
        try:
            await methods[params[0]](data, params, messageUser, message)
        except:
            log_message("{} is not a valid command".format(params[0]))
    elif is_admin(data, messageUser):
        office_hours_newTeacher(data, params, message)
    else:
        log_message("{} has insufficent permissions".format(messageUser))

    file.close()
    file = open("officeHours.json", "w")
    json.dump(data, file)

# --------------------------------------------------
# Checks to see if the user is a teacher
#
# @param data - from the json object
# @param user - that requested the command
# @return bool - status of admin
# --------------------------------------------------


def is_teacher(data, user):
    try:
        teacher = data['TEACHERS'][user.upper()]
    except:
        log_message(
            "{} does not have permission to modify office hours".format(user))
        return False
    return True

# --------------------------------------------------
# checks to see if user is an admin
#
# @param data - from the json object
# @param user - that requested the command
# @return bool - status of admin
# --------------------------------------------------


def is_admin(data, user):
    return user in data["ADMINS"]

# --------------------------------------------------
# Method to process adding of office hours
#
# @Command !officeHours -add <DAY> <START TIME> <END TIME>
#
# @param data - from the json object
# @param params - passed in with the command
# @param user - that requested the command
# @return none
# --------------------------------------------------


async def office_hours_add(data, params, user, message):
    log_message("Process Adding New Office Hours ...")
    teacher = data['TEACHERS'][user.upper()]

    teacher[params[1]] = {"START": params[2], "END": params[3]}
    log_message("Process Complete!")

    embedVar = discord.Embed(title="Office Hours Added", color=0x00ff00)
    embedVar.add_field(
        name=params[1], value=get_time(params[2]) + " - " + get_time(params[3]), inline=False)
    await message.channel.send(embed=embedVar)

# --------------------------------------------------
# Method to process editing of office hours
#
# @Command !officeHours -edit <DAY> <START TIME> <END TIME>
#
# @param data - from the json object
# @param params - passed in with the command
# @param user - that requested the command
# @return none
# --------------------------------------------------


async def office_hours_edit(data, params, user, message):
    log_message("Process Editing Office Hours ...")
    teacher = data['TEACHERS'][user.upper()]

    teacher[params[1]]["START"] = params[2]
    teacher[params[1]]["END"] = params[3]

    log_message("Process Complete!")

    embedVar = discord.Embed(title="Office Hours Updated", color=0x00ff00)
    embedVar.add_field(
        name=params[1], value=get_time(params[2]) + " - " + get_time(params[3]), inline=False)
    await message.channel.send(embed=embedVar)

# --------------------------------------------------
# Method to process deletion of office hours
#
# @Command !officeHours -delete <DAY>
#
# @param data - from the json object
# @param params - passed in with the command
# @param user - that requested the command
# @return none
# --------------------------------------------------


async def office_hours_delete(data, params, user, message):
    log_message("Process Deleting Office Hours ...")

    teacher = data['TEACHERS'][user.upper()]

    teacher.pop(params[1], None)

    log_message("Process Complete!")

    embedVar = discord.Embed(title="Office Hours Removed", color=0x00ff00)
    embedVar.add_field(name=params[1], value="-", inline=False)
    await message.channel.send(embed=embedVar)

# --------------------------------------------------
# Method to list of office hours
#
# @Command !officeHours -list
#
# @param data - from the json object
# @param params - passed in with the command
# @param user - that requested the command
# @return none
# --------------------------------------------------


async def office_hours_list(data, params, user, message):
    log_message("Process List Office Hours ...")

    teacher = data['TEACHERS'][user.upper()]

    log_message("Process Complete!")

    embedVar = discord.Embed(title="Office Hours Removed", color=0x00ff00)
    for key in teacher:
        embedVar.add_field(
            name=key, value=teacher[key]["START"] + " - " + teacher[key]["END"], inline=False)
    await message.channel.send(embed=embedVar)

# --------------------------------------------------
# Method to process adding a new teacher
#
# @Command !officeHours -newTeacher <TEACHER NAME>
#
# @param data - from the json object
# @param params - passed in with the command
# @return none
# --------------------------------------------------


async def office_hours_newTeacher(data, params, message):
    log_message("Process Adding New Teacher ...")

    if(params[0] == "-NEWTEACHER"):
        data["TEACHERS"][params[1]] = {}

    log_message("Process Complete!")

    embedVar = discord.Embed(title="New Teacher Added", color=0x00ff00)
    embedVar.add_field(name=params[1], value="-", inline=False)
    await message.channel.send(embed=embedVar)


# --------------------------------------------------
# Get 12 hour time
#
# @param time - 24 hour timestamp
# @return 12 hour timestamp
# --------------------------------------------------
def get_time(time):
    return datetime.datetime.strptime(
        time, '%H:%M').time().strftime("%I:%M %p")
