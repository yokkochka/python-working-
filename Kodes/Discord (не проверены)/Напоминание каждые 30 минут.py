import discord
import credits
import asyncio
from discord.ext import commands, tasks
import random

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.token


@bot.event
async def on_message(message):
    parse_str = message.content
    parse_str = parse_str.capitalize()
    word_list = parse_str.split(" ")
    if "Запуск" in word_list:
        while True:
            await message.channel.send("Будильник сработает через 30 минут")
#             await asyncio.sleep(5)    #  Для проверки работоспособности
            await asyncio.sleep(1800) 
            await message.channel.send("Время сделать мини зарядку")
            
bot.run(token)