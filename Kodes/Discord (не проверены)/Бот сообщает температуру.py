import discord
import credits
import random
from ramapi import *
from discord.ext import commands
from ramapi import Character


client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.token

@bot.command(name="start")
async def start(ctx):
    await ctx.send("Hi ")
    
@bot.command(name='name')
async def name(ctx, character):
    counter = 0
    result = ' '
    characters = Character.filter(name=character)
    for i in characters['results']:
        result = 'Имя: ' + i['name'] + '\n' + 'Вид: ' + i['species'] + '\n' + 'Статус: ' + i['status'] + '\n' + 'Пол: ' + i['gender'] + '\n' + 'Место рождения: ' + i['origin']['name'] + '\n' + 'Место нахождения: ' + i['location']['name'] + '\n' + '\n'
        counter += 1
        if counter == 5:
            break
    await ctx.send(result)
    

bot.run(token)