#!/usr/bin/env python3
import discord
import markopy.marko
from typing import Callable, Awaitable
from functor import Contains, StartsWith, And, Not, Equals
from action import SendResponse, MarkovGenerator

class BotClient(discord.Client):
    def __init__(self, commands):
        discord.Client.__init__(self)
        self.commands = commands
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author != self.user:
            for command in self.commands:
                if command[0](message.content):
                    try:
                        await command[1](message)
                    except ex:
                        print(str(ex))

class Bot(object):
    def __init__(self):
        self.auth = self.read_auth('auth.txt')
        self.help_text = self.read_help('help.txt')
        self.strings = self.read_strings('strings.txt')
        self.commands = [
            (Contains('yoshi'), SendResponse(self.strings['yoshi'])),
            (Contains('uwu'), SendResponse(self.strings['uwu'])),
            (And(StartsWith('>tfw'), Not(StartsWith('>tfwnogf'))), SendResponse(self.strings['tfw'])),
            (StartsWith('>tfwnogf'), SendResponse(self.strings['tfwnogf'])),
            (Equals('turn that poop'), SendResponse('into wine')),
            (Equals('>sophistry'), MarkovGenerator('republic.txt')),
            (Equals('>help'), SendResponse(self.help_text))
        ]
        self.client = BotClient(self.commands)

    def run(self):
        self.client.run(self.auth)

    def read_auth(self, path: str) -> str:
        with open(path, mode='r') as file:
            return file.readline().strip(' \n\r')

    def read_strings(self, path: str) -> dict:
        with open(path, mode='r') as file:
            strings = {}
            for line in  file:
                key, value = line.partition('=')[::2]
                strings[key.strip()] = value
            return strings

    def read_help(self, path: str) -> str:
        with open('help.txt', 'r') as file:
            return file.read()


def main():
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()