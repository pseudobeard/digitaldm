import discord
from discord.ext import commands
#import helper
import dicetower
import pickle
import glob
import time

description = 'Digital DM fudges rolls in accordance with py.rand'
bot = commands.Bot(command_prefix='.', description=description)
#helper = helper.Helper()
dicetower = dicetower.Dicetower()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('Loading players from pickles')
#    known_players.extend(helper.loadPlayers())
    print('DIGITAL DM READY')


@bot.command(description='Roll one or more dice')
async def roll(*args):
    #Need to do this to roll a "default" dice
    args_list = list(args)
    result = 0
    if len(args_list) == 0:
        await bot.say("No dice specified. Assuming 1d20")
        args_list.append('1d20')
    print(args_list)
    for dice in args_list:
        dice.split('d')
        print(dice)
        result = result + dicetower.roll('20')


    await bot.say("Rolled a " + result)

# @bot.command(description='Balance teams in scrim by a certain weight')
# async def autobalance(*args):
#     if len(args) == 0:
#         await bot.say("Please provide one or more weights to balance")
#         return
#
#     args = list(args) # convert args to list (was tuple) for easy removal of "--no2CP" arg
#
#     no2CP = False
#     if "--no2CP" in args:
#         no2CP = True
#         args.remove("--no2CP") # Remove "--no2CP" so it does not get treated as a weight name later
#
#     active_players = []
#     for p in known_players:
#         if p.getStatus() == "Active":
#             active_players.append(p)
#     message_list = []
#     for weight in args:
#         sc = scrim.Scrim(weight)
#         status, red_team, blue_team = balancer.partition(active_players, weight) # TODO: convert to multi-team (>2) partition function
#         await bot.say(status)
#         sc.setTeams(red_team, blue_team)
#         message_list.append(balancer.printTeam("Red Team", red_team, weight))
#         message_list.append(balancer.printTeam("Blue Team", blue_team, weight))
#         scrims.append(sc)
#     for message in message_list:
#         s_message = helper.serializeMessage(message)
#         await bot.say(s_message)
#     await bot.say("```Random map: '" + mapHandler.getMap(no2CP) + "'```")


bot.run('MzQ4NjAwNTU1MTg0MTkzNTM2.DHpWcg.PEEY0WB-V2VVa7hjq-4AZ87jWJE')

