def read_strings(path: str) -> object:
    with open(path, mode='r') as file:
        strings = {}
        for line in file:
            key, value = line.partition('=')[::2]
            strings[key.strip()] = value
        return strings


strings = read_strings('strings.txt')