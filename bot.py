#!/usr/bin/env python3
import discord

class And(object):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    def __call__(self, string: str) -> bool:
        return self.lhs(string) and self.rhs(string)

class Not(object):
    def __init__(self, pred):
        self.pred = pred
    def __call__(self, string: str) -> bool:
        return not self.pred(string)

class SendResponse(object):
    def __init__(self, rspns: str):
        self.response = rspns
    async def __call__(self, message: discord.Message):
        await message.channel.send(self.response)

class Contains(object):
    def __init__(self, txt: str, ignore_case: bool = True):
        self.text = txt
        if ignore_case:
            self.text = self.text.lower()
        self.ignore_case = ignore_case
    def __call__(self, string:str) -> bool:
        if self.ignore_case:
            string = string.lower()
        return self.text in string

class StartsWith(object):
    def __init__(self, txt: str, ignore_case: bool = True):
        self.text = txt
        if ignore_case:
            self.text = self.text.lower()
        self.ignore_case = ignore_case
    def __call__(self, string: str) -> bool:
        if self.ignore_case:
            string = string.lower()
        return string.startswith(self.text)

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

async def handle_command(message):
    for command in commands:
        if command[0](message.content):
            await command[1](message)

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author != self.user:
            await handle_command(message)

def start_client():
    client = BotClient()
    client.run(auth)

def main():
    start_client()

if __name__ == '__main__':
    main()