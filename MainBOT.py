from asyncio import tasks
from enum import auto
from discord import File
from discord.ext import tasks, commands
from tracemalloc import start
from data import stocks
import discord
import ctx
import os


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$stocks'):
        for stock in stocks:
            if stocks[stock][-1] > 70:
                await message.channel.send('Sell ' + stock + ', RSI: ' + str(int(stocks[stock][-1])))
                await message.channel.send(file=discord.File("pictures/" + stock + ".png"))

            elif stocks[stock][-1] < 30:
                await message.channel.send('Buy ' + stock + ', RSI: ' + str(int(stocks[stock][-1])))
                await message.channel.send(file=discord.File("pictures/" + stock + ".png"))

client.run('Insert Discord Token here')
