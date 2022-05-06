from asyncio import tasks
from enum import auto
from discord import File
from discord.ext import tasks, commands
from tracemalloc import start
from data import stocks
import discord
import ctx
import os

bot = commands.Bot("!")

target_channel_id = ('Text channel ID')
#Höger klicka på text kanal sedan copy channel ID

@tasks.loop(hours=12)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    for stock in stocks:
        if stocks[stock][-1] > 70:
            embed = discord.Embed(
            title=stock, description=('Sell ' + stock + ', RSI: ' + str(int(stocks[stock][-1]))),
            colour=discord.Colour.purple()
            )
            await message_channel.send(embed=embed, file=discord.File("pictures/" + stock + ".png"))

        elif stocks[stock][-1] < 30:
            embed = discord.Embed(
                title=stock,
                description=('Buy ' + stock + ', RSI: ' +
                             str(int(stocks[stock][-1]))),
                colour=discord.Colour.purple()
            )
            await message_channel.send(embed=embed, file=discord.File("pictures/" + stock + ".png"))


@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
bot.run("Discord Bot Token")
#använd https://discord.com/developers/applications/ för att skapa en bot för att sedan gå undder bot och hämta token genom reset token
