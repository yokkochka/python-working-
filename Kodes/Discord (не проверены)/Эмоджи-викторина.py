import discord
import credits
import asyncio
from discord.ext import commands, tasks
from random import choice

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.token

@bot.event
async def on_message(message):
    if message.content.startswith("д") or message.content.startswith("дай загадку"):
        
        numbers = [1, 2, 3, 4, 5, 6]
        num = choice(numbers)
        answer = 0
        if num == 1:
            await message.channel.send('\U0001F920' '\U0001F44D' "\U0001F920" "\U0001F920" '\U0001F44D' '\U0001F44D')
            await message.channel.send('Как думаешь, что это за пословица?')
            answer = await bot.wait_for('message')
            await message.channel.send('Ответ: одна голова хорошо, а две лучше')
        if num == 2:
            await message.channel.send('\U0001F30D' '\U0001F435')
            await message.channel.send('Как думаешь, какой фильм зашифрован?')
            answer = await bot.wait_for('message')
            await message.channel.send('Ответ: планета обезьян')
        if num == 3:
            await message.channel.send('\U0001F608' '\U0001F457' '\U0001F460')
            await message.channel.send('Как думаешь, какой фильм зашифрован?')
            answer = await bot.wait_for('message')
            await message.channel.send('Ответ: дьявол носит "Prada"')
        if num == 4:
            await message.channel.send('\U0001F3AE' '\U0001F991')
            await message.channel.send('Как думаешь, какой фильм зашифрован?')
            answer = await bot.wait_for('message')
            await message.channel.send('Ответ: игра в кальмара')

        if num == 5:
            await message.channel.send('\U0001F920' '\U0001F590' '\U0001F590' ':scissors:')
            await message.channel.send('Как думаешь, какой фильм зашифрован?')
            answer = await bot.wait_for('message')
            await message.channel.send('Ответ: Эдвард руки-ножницы')
            
bot.run(token)