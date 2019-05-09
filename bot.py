#!/usr/bin/env python3
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

auth = ''
with open('auth.txt') as file:
	line = file.readline()
	auth = line

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

@bot.command()
async def yoshi(ctx):
	await ctx.send('https://i.imgur.com/kW80dMz.jpg')

print('running...')
bot.run(auth)