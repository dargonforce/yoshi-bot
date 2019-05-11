#!/usr/bin/env python3
import discord
import auth
from action import Action
from functools import partial
from commands import commands


class BotClient(discord.Client):
    def __init__(self, message_callback):
        discord.Client.__init__(self)
        self.message_callback = message_callback

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author != self.user:
            await self.message_callback(message)


class Bot(object):
    def __init__(self):
        self.auth = auth.get_auth()
        self.commands = commands
        self.client = BotClient(partial(self.handle_message))

    async def handle_message(self, message: discord.Message):
        for command in self.commands:
            if command[0](message.content):
                try:
                    await command[1].action(message)
                except Exception as ex:
                    print(str(ex))

    def run(self):
        self.client.run(self.auth)


if __name__ == '__main__':
    bot = Bot()
    bot.run()
