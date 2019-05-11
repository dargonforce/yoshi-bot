import random
import discord
import markopy.marko as marko


class Action(object):
    def __init__(self):
        pass

    async def invoke(self, message: discord.Message):
        pass

    async def __call__(self, message: discord.Message):
        await self.invoke(message)


class SendResponse(Action):
    def __init__(self, rspns: str):
        Action.__init__(self)
        self.response = rspns

    async def invoke(self, message: discord.Message):
        await message.channel.send(self.response)


class SendFile(Action):
    def __init__(self, path: str):
        Action.__init__(self)
        self.path = path

    async def invoke(self, message: discord.Message):
        with open(self.path) as file:
            await message.channel.send(file=file)


class MarkovGenerator(Action):
    def __init__(self, path: str):
        Action.__init__(self)
        self.path = path
        self.word_list = marko.text_to_training_data(self.path)

    async def invoke(self, message: discord.Message):
        await message.channel.send(self.build_line())

    def build_line(self):
        words = [random.choice(list(self.word_list.keys())).title()]
        while True:
            words.append(random.choice(self.word_list[words[-1].lower()]))
            if words[-1][-1] == '.':
                break
        line = words[0]
        for word in words[1:-1]:
            line = line + ' ' + word
        line += '.'
        return line


class PrintHelpText(Action):
    def __init__(self):
        Action.__init__(self)
        with open('help.txt') as file:
            self.help_text = file.read()

    async def invoke(self, message: discord.Message):
        await message.channel.send(self.help_text)


if __name__ == '__main__':
    gen = MarkovGenerator('republic.txt')
    print(gen.build_line())
