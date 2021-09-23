# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        )


@bot.command(name='funny', help='Responds with a random quote from funny')
async def funny(ctx):
    
    funny_quotes = [
        'I’m sick of following my dreams, man. I’m just going to ask where they’re going and hook up with ’em later.',
        'A pessimist is a person who has had to listen to too many optimists.',
        'Better to remain silent and be thought a fool than to speak out and remove all doubt.',
        'Don’t worry about the world coming to an end today. It is already tomorrow in Australia.',
    ]

    response = random.choice(funny_quotes)
    await ctx.send(response)

bot.run(TOKEN)
