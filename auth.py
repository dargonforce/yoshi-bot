import os
from pathlib import Path

file_path = 'auth.txt'
env_var = 'DISCORD_AUTH_KEY'

def get_auth():
    if Path(file_path).exists():
        with open(file_path, 'r') as file:
            return file.read().strip('\n\r ')
    else:
        return os.environ[env_var]
