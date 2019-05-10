#!/usr/bin/env python3
import discord
import markopy.marko
from functor import Contains, StartsWith, And, Not

class SendResponse(object):
    def __init__(self, rspns: str):
        self.response = rspns
    async def __call__(self, message: discord.Message):
        await message.channel.send(self.response)

with open('strings.txt') as file:
    strings = {}
    for line in  file:
        key, value = line.partition('=')[::2]
        strings[key.strip()] = value

with open('auth.txt') as file:
    auth = file.readline().strip(' \n\r')

commands = [
    (Contains('yoshi'), SendResponse(strings['yoshi'])),
    (Contains('uwu'), SendResponse(strings['uwu'])),
    (And(StartsWith('>tfw'), Not(StartsWith('>tfwnogf'))), SendResponse(strings['tfw'])),
    (StartsWith('>tfwnogf'), SendResponse(strings['tfwnogf']))
]

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author != self.user:
            for command in commands:
                if command[0](message.content):
                    await command[1](message)

def start_client():
    client = BotClient()
    client.run(auth)

def main():
    start_client()

if __name__ == '__main__':
    main()