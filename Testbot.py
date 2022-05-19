from asyncio import tasks
from enum import auto
from lib2to3.pgen2.token import NEWLINE
from re import S
from discord import File
from discord.ext import tasks, commands
from tracemalloc import start
from matplotlib.pyplot import title
from data import stocks
import discord
import ctx
import os


client = discord.Client()
client = commands.Bot("$")
target_channel_id = 973478588265406524

@tasks.loop(hours=12)
async def called_once_a_day():
    message_channel = client.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    for stock in stocks:
        if stocks[stock][-1] > 70:
            embed = discord.Embed(
                title=stock, description=(
                    'Sell ' + stock + ', RSI: ' + str(int(stocks[stock][-1]))),
                colour=discord.Colour.dark_gray()
            )
            await message_channel.send(embed=embed, file=discord.File("pictures/" + stock + ".png"))

        elif stocks[stock][-1] < 30:
            embed = discord.Embed(
                title=stock,
                description=('Buy ' + stock + ', RSI: ' +
                             str(int(stocks[stock][-1]))),
                colour=discord.Colour.dark_gray()
            )
            await message_channel.send(embed=embed, file=discord.File("pictures/" + stock + ".png"))


@called_once_a_day.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    med = ''
    med2 = ''
    if message.author == client.user:
        return
    for stock in stocks:
        med += str(stock) + '\n'
    if message.content.startswith('$stocklist'):
        embed2 = discord.Embed(
        title = 'Stock List',
        description = med)
        await message.channel.send(embed=embed2) 
    if message.content.startswith('$stock'):
        name = message.content.split(' ')
        name = name[1]
        V1 = stocks[name]
        name= str(name)
        X = ''
        # for V in V1:
        k = 0
        while k < 3:
            X += str(V1[-k]) + '\n'
            k += 1
        embed2 = discord.Embed(
        title=name,
        description = "RSI:" '\n' + X)
        colour = discord.Colour.dark_gray()
        await message.channel.send(embed=embed2)

    if message.content.startswith('$help'):
        embed1 = discord.Embed(
        title= 'Commands',
        description= str('$Stocklist for a list of multiple stocks' + '\n' + '$stock (name) for info on single stock'),
        colour=discord.Colour.dark_gray())
        await message.channel.send(embed=embed1)


#Höger klicka på text kanal sedan copy channel ID

client.run("token")

