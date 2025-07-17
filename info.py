import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'TechVJBot')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '28269435'))
API_HASH = environ.get('API_HASH', '839f282133fe8ee79b4a946095cf4360')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "7811341300:AAHAsHowVA5XKloH1U7LW3PPd_FkhEGWgZM")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '8005648537'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "7811150842:AAFCnH0eZFi90IY_LrHM8NK5Z4qpZfcrIAA")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002691497570'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://Hanuman:hanuman@cluster0.l5toshc.mongodb.net/?retryWrites=true&w=majority")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", "")

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", "https://hprajmovies.blogspot.com/p/p.html")

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
