import discord
import credits
import asyncio
from discord.ext import commands, tasks

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = credits.token

@bot.command(name="timer")
async def timer(ctx, number):
    number = int(number)
    message = await ctx.send(number)
    while number != 0:
        number -= 1
        await message.edit(content=number)
        await asyncio.sleep(1)
    await message.edit(content='Ended!')

bot.run(token)