import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot Active.')

@client.command()
async def greet(ctx):
    await ctx.send('Hello, how are you?')

client.run('ODk0OTkxNDIyMTE2MjI1MDQ0.YVyDtw.UU1ZBviDhaQbfPPytEZZUwkXCrE')