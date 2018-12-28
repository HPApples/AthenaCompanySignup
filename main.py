# Work with Python 3.6
import discord
import asyncio
import sqlite3

from discord.ext import commands

TOKEN = 'NTAyNTEwMzYwMzY5MTY4Mzk0.DqthbA.Z-X8-pCU7KrpvELqt6FlHkM-tuQ'

initial_extensions = ['commandListener','event', "role"]

bot = commands.Bot(command_prefix=('!'))
bot.pm_help = True
bot.owner_ID = ('102170338942517248')

bot.remove_command("help")

if __name__ == '__main__':
    for extension in initial_extensions:
        # try:
            bot.load_extension(extension)
        # except Exception as e:
        #     print(f'failed to load extension {extension}')

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Game(name="Terry Big Gay", type=2))

bot.run(TOKEN)