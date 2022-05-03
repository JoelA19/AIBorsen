from asyncio import tasks
from enum import auto
from discord.ext import tasks, commands
from tracemalloc import start
import discord
import ctx
import os

from data import stock
from Stonks import stocks

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
def alert(alerted):
        if stocks[stock][-1] > 70:
            alerted.channel.send('Sell ' + stock + ', RSI:', int(stocks[stock][-1]))
        
        if stocks[stock][-1] < 30:
            alerted.channel.send('Buy ' + stock + ', RSI:', int(stocks[stock][-1]))


client.run('OTU2NTk0MjA5NjY0NjkyMjY0.YjyfyA.gbI46Rx2rtrq9s9vtD5jBSAGw-Y')
