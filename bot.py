#!/usr/bin/env python3
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>', description='Yoshi Bot')

with open('auth.txt') as file:
    auth = file.readline().strip(' \n\r')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def yoshi(ctx):
    await ctx.send('https://i.imgur.com/v1K2rxK.png')

@bot.command()
async def tfw(ctx):
	await ctx.send('https://i.imgur.com/02VZNGr.jpg')

@bot.command()
async def tfwnogf(ctx):
	await ctx.send('https://i.imgur.com/xarhxj4.jpg')

print('running...')
bot.run(auth)
