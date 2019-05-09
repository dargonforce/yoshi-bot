#!/usr/bin/env python3
import discord

with open('strings.txt') as file:
	strings = {}
	for line in  file:
		key, value = line.partition('=')[::2]
		strings[key.strip()] = value

with open('auth.txt') as file:
    auth = file.readline().strip(' \n\r')

class BotClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message(self, message):
		if message.author != self.user:
			if message.content == 'ping':
				await message.channel.send('pong')
			if 'yoshi' in message.content:
				await message.channel.send(strings['yoshi'])
			elif message.content == '>tfwnogf':
				await message.channel.send(strings['tfwnogf'])
			elif message.content.startswith('>tfw'):
				await message.channel.send(strings['tfw'])

client = BotClient()
client.run(auth)