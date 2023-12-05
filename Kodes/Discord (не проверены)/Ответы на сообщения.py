# import discord
# import credits
# from discord.ext import commands
# 
# client = discord.Client()
# bot = commands.Bot(command_prefix='!')
# token = credits.bot_token
# 
# @bot.event
# async def on_message(message):
#     if message.content.startswith("Привет"):
#         await message.reply("Рад тебя видеть снова!", mention_author=True)
# 
# 
# bot.run(token)

import discord
import credits
import asyncio
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.bot_token

@bot.event
async def on_message(message):
    if message.content.startswith("Привет"):
        await message.reply("Рад тебя видеть снова! Как твои дела?", mention_author=True)
    if message.content.startswith("Нормально"):
        await message.reply("Ясно! А как погода в твоем городе?", mention_author=True)
    if message.content.startswith("Хорошо"):
        await message.reply("Ясно! А как погода в твоем городе?", mention_author=True)
    if message.content.startswith("Плохо"):
        await message.reply("Ясно! А как погода в твоем городе?", mention_author=True)

        

bot.run(token)