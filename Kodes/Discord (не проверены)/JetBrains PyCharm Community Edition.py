import discord
import credits
import os
import random
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.token

game_dictionary = {}
member_list = []
screen_dictionary = {}

@bot.command(name="start")
async def start(ctx):
    global member_list
    if ctx.author.name in member_list:
        await ctx.send("Ты уже со мной здоровался - я тебя знаю " + ctx.author.name)
    else:
        await ctx.send("Привет, " + ctx.author.name + "! Добро пожаловать ко мне!")
        member_list.append(ctx.author.name)
    os.mkdir(ctx.author.name)
    
    global game_dictionary
    if ctx.author.name not in game_dictionary:
        game_dictionary[ctx.author.name] = []

    global screen_dictionary
    if ctx.author.name not in screen_dictionary:
        screen_dictionary[ctx.author.name] = []
    

bot.run(token)