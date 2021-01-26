import os
import time
import discord
import pyautogui as pag
from discord.ext import commands


with open('token.txt', 'r') as f:
    TOKEN = f.read()

bot = commands.Bot('!')

# Initialising

# Commands go here
def pressKey(key):
    pag.keyDown(key)
    time.sleep(0.1)
    pag.keyUp(key)
    time.sleep(0.5)

async def ss(ctx, ):
    shot = pag.screenshot('shot.png')
    await ctx.send(file=discord.File('shot.png'))

@bot.command()
async def sayhi(ctx, ):
    await ctx.send('Hello!')

@bot.command()
async def up(ctx):
    pressKey('up')
    await ss(ctx)

@bot.command()
async def down(ctx, ):
    pressKey('down')
    await ss(ctx)

@bot.command()
async def left(ctx, ):
    pressKey('left')
    await ss(ctx)

@bot.command()
async def right(ctx, ):
    pressKey('right')
    await ss(ctx)

@bot.command()
async def a(ctx, ):
    pressKey('d')
    await ss(ctx)

@bot.command()
async def b(ctx, ):
    pressKey('s')
    await ss(ctx)

# ------------------

bot.run(TOKEN)
