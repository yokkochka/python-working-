# import discord

# import credits
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.token


# @bot.command(name='start')
# async def start(ctx):
#     await ctx.send("Привет - я твой первый Discord-бот и я готов выполнять команды")
#     
#     
# @bot.command(name='credits')
# async def start(ctx):
#     await ctx.send("Здесь должна быть какая-нибудь информация")

@bot.event
async def on_message(message):
    if message.content == 'Привет':
        await message.channel.send("Я рад тебя видеть")
        
        
@bot.event
async def on_message_delete(message):
    await message.channel.send("Сообщение удалено")

@bot.event
async def on_message(message):
    parse_str = message.content
    parse_str = parse_str.capitalize()
    word_list = parse_str.split(" ")
    if "Игра" in word_list:
        await message.channel.send("Кто-то сказал игра?")


bot.run(token)
