import discord
import credits
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.bot_token


@bot.event
async def on_message(message):
    if message.content.startswith("Привет"):
        await message.channel.send(":wave:")
    if message.content.startswith("Круто"):
        await message.channel.send(":thumbsup:")
    if message.content.startswith("Огонь"):
        await message.channel.send(":boom:")
    if message.content.startswith("Ок"):
        await message.channel.send(":ok_hand:")
    if message.content.startswith("Люблю"):
        await message.channel.send(":heart:")


bot.run(token)