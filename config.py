from os import environ, getenv

from dotenv import load_dotenv

NORMAL_COLOR = 0x2B2D31
INFORMATION_COLOR = 0x546E7A
WARNING_COLOR = 0xE67E22
ERROR_COLOR = 0xE74C3C

if 'RAILWAY_ENVIRONMENT' not in environ:
    load_dotenv()


print('Token length:', len(environ['TOKEN']))
TOKEN = environ['TOKEN']
STAFF_ROLE_ID = getenv('STAFF_ROLE_ID')

DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_PASSWORD = getenv('DB_PASSWORD')

AWAIZ_USER_ID = '434096457927360513'
BOOKCLUB_CHANNEL_ID = '1226246395351007334'
