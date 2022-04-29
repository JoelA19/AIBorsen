from asyncio import tasks
from enum import auto
from discord.ext import tasks, commands
from tracemalloc import start
import discord
import ctx
import os

from data import RSI

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        await message.channel.send('Bot is functioning')

    elif message.content.startswith('$chart'):
        await message.channel.send(file=discord.File('insert path'))

@tasks.loop(hours = 1.0)
async def auto_send(statement):
    statement.channel = await client.fetch.channel('509390855703101452')
    if RSI == [14]: 
        statement.channel.send('RSI under 14')

    elif RSI == [30]:
        statement.channel.send('RSI over 30')


client.run('OTU2NTk0MjA5NjY0NjkyMjY0.YjyfyA.RVHggdRh3oYtydZDdLsYGjrtMWI')
