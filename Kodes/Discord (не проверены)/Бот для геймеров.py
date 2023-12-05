import discord
import credits
import os
import random
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.bot_token

game_dictionary = {}
member_list = []
screen_dictionary = {}


@bot.command(name="start")
async def start(ctx):
    global member_list
    if ctx.author.name in member_list:
        await ctx.send("Ты уже со мной здоровался - я тебя знаю " + ctx.author.name)
    else:
        member_list.append(ctx.author.name)
        os.mkdir(ctx.author.name)
        await ctx.send("Привет, " + ctx.author.name + "! Добро пожаловать ко мне!")
    global game_dictionary
    if (ctx.author.name in game_dictionary.keys()) == False:
        game_dictionary[ctx.author.name] = []
    global screen_dictionary
    if (ctx.author.name in screen_dictionary.keys()) == False:
        screen_dictionary[ctx.author.name] = []


@bot.command(name="addgame")
async def addgame(ctx, message):
    game_list = game_dictionary.get(ctx.author.name)
    game_list.append(str(message))
    game_dictionary[ctx.author.name] = game_list


@bot.command(name="showmygames")
async def showmygames(ctx):
    await ctx.send("Cписок игр, в которые ты играешь - " + str(game_dictionary.get(ctx.author.name)))


@bot.command(name="sendscreen")  # Отправляем через "Добавить комментарий"
async def sendscreen(ctx):
    for attach in ctx.message.attachments:
        await attach.save(ctx.author.name + "/" + attach.filename)
        screen_list = screen_dictionary.get(ctx.author.name)
        screen_list.append(ctx.author.name + "/" + attach.filename)
        screen_dictionary[ctx.author.name] = screen_list


@bot.command(name="getlastscreen")
async def getlastscreen(ctx):
    screen_list = screen_dictionary.get(ctx.author.name)
    last_screen_path = screen_list[-1]
    await ctx.send(file=discord.File(last_screen_path))




bot.run(token)
