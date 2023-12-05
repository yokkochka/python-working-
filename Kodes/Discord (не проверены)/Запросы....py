import discord
import credits
import random
from ramapi import *
from discord.ext import commands
from ramapi import Character


client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.token

characters = Character.filter(name='Morty Smith')

for character in characters['results']:
    print('Имя:', character['name'])
    print('Вид:', character['species'])
    print('Статус:', character['status'])
    print('Пол:', character['gender'])
    print('Место рождения:', character['origin']['name'])
    print('Место нахождения:', character['location']['name'])


bot.run(token)


