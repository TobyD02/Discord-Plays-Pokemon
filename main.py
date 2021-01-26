import os
import discord
import pyautogui as pag
from discord.ext import commands

with open('token.txt', 'r') as f:
    TOKEN = f.read()

bot = commands.Bot('!')

# Commands go here
os.system('open pokemonEmerald.gba')

async def ss(ctx, ):
    shot = pag.screenshot('shot.png')
    await ctx.send(file=discord.File('shot.png'))

@bot.command()
async def sayhi(ctx, ):
    await ctx.send('Hello!')

@bot.command()
async def up(ctx):
    pag.press('up')
    await ss(ctx)

@bot.command()
async def down(ctx, ):
    pag.press('down')
    await ss(ctx)

@bot.command()
async def left(ctx, ):
    pag.press('left')
    await ss(ctx)

@bot.command()
async def right(ctx, ):
    pag.press('right')
    await ss(ctx)

@bot.command()
async def a(ctx, ):
    pag.press('a')
    await ss(ctx)

@bot.command()
async def b(ctx, ):
    pag.press('b')
    await ss(ctx)

# ------------------

bot.run(TOKEN)
