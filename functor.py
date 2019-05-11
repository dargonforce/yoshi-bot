from typing import Callable


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


class Equals(object):
    def __init__(self, text: str, ignore_case: bool = True):
        self.text = text
        if ignore_case:
            self.text = self.text.lower()
        self.ignore_case = ignore_case

    def __call__(self, string: str) -> bool:
        if self.ignore_case:
            string = string.lower()
        return string == self.text


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


class And(object):
    def __init__(self, *params: Callable[[str], bool]):
        self.params = params

    def __call__(self, string: str) -> bool:
        return all(map(lambda x: x(string), self.params))


class Or(object):
    def __init__(self, *params: Callable[[str], bool]):
        self.params = params

    def __call__(self, string: str) -> bool:
        return any(map(lambda x: x(string), self.params))


class Not(object):
    def __init__(self, predicate: Callable[[str], bool]):
        self.predicate = predicate

    def __call__(self, string: str) -> bool:
        return not self.predicate(string)
