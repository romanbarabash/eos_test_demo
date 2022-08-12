from environs import Env

env = Env()
env.read_env(verbose=True)

TIMEOUT = env.int('TIMEOUT')
HOST = env.str('HOST')

GMAIL_USER_ID = env.str('GMAIL_USER_ID')
CLIENT_ID = env.str('CLIENT_ID')
CLIENT_SECRET = env.str('CLIENT_SECRET')
REFRESH_TOKEN = env.str('REFRESH_TOKEN')
TOKEN_URI = env.str('TOKEN_URI')
