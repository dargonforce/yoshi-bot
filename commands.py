from typing import List, Tuple, Callable
from command import Command
from functor import Contains, And, StartsWith, Equals, Not
from action import SendResponse, MarkovGenerator, PrintHelpText
from config import strings

commands: List[Tuple[Callable[[str], bool], Command]] = [
    (Contains('yoshi'), Command(SendResponse(strings['yoshi']))),
    (Contains('uwu'), Command(SendResponse(strings['uwu']))),
    (And(StartsWith('>tfw'), Not(StartsWith('>tfwnogf'))), Command(SendResponse(strings['tfw']))),
    (StartsWith('>tfwnogf'), Command(SendResponse(strings['tfwnogf']))),
    (Equals('turn that poop'), Command(SendResponse('into wine'))),
    (Equals('>sophistry'), Command(MarkovGenerator('republic.txt'))),
    (Equals('>help'), Command(PrintHelpText()))
]