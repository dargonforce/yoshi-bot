import discord
import markopy.marko as marko
import random

class Action(object):
    def __init__(self):
        pass
    async def invoke(message: discord.Message):
        pass
    async def __call__(self, message: discord.Message):
        await self.invoke(message)

class SendResponse(Action):
    def __init__(self, rspns: str):
        self.response = rspns
    async def invoke(self, message: discord.Message):
        await message.channel.send(self.response)

class SendFile(Action):
    def __init__(self, path: str):
        self.path = path
    async def invoke(self, message: discord.Message):
        with open(self.path) as file:
            await message.channel.send(file=file)

class MarkovGenerator(Action):
    def __init__(self, path: str):
        self.path = path
        self.wordlist = marko.text_to_training_data(self.path)
    async def invoke(self, message: discord.Message):
        await message.channel.send(self.build_line())
    def build_line(self):
        words = [random.choice(list(self.wordlist.keys())).title()]
        while True:
            words.append(random.choice(self.wordlist[words[-1].lower()]))
            if words[-1][-1] == '.':
                break
        line = words[0]
        for word in words[1:-1]:
            line = line + ' ' + word
        line += '.'
        return line

if __name__ == '__main__':
    gen = MarkovGenerator('republic.txt')
    print(gen.build_line())