import os
from pathlib import Path

file_path = 'auth.txt'
env_var = 'DISCORD_AUTH_KEY'

def get_auth():
    if Path(file_path).exists():
        with open(file_path, 'r') as file:
            return file.read().strip('\n\r ')
    else:
        try:
            return os.environ[env_var]
        except KeyError:
            return None

if __name__ == '__main__':
    print(get_auth())
