import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "14579176"))
API_HASH = getenv("API_HASH", "39ac717c9b38891c6a4351fe8ea376f2")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8287823604:AAHt3Q0ymjikNChgl8949lBxb0Ulc_N9S3g")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mahavirkumar:mahavirkumar>@cluster0.3t52j36.mongodb.net/?appName=Cluster0)"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1700))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1003904556542"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "8329778041"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

API_URL = getenv("API_URL", "https://apisparrow.site") #youtube song url
API_KEY = getenv("API_KEY", None) # Get This API KEY FROM OWNER: @SpYtAPIBot

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DevloperSP/MusicSp",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+AEbif9fb9pszODM1") 
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+KrBRT9foT-ljMTFl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-MusicSp-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", BQDedegAJ_j1m6gjqA30-T_cSW5tlPYwIS5i82wO0EgfjvmIGTg5OInwHIrDzTfnmZsg_v-4x-3TetbW7lz4eEb7LxZVbfQoBLXDRCJI7PmIYzHArxh0VuedBVUwb04ChjveRs37yoP9dZbmo4Ve2xeB1fqzT8bNg_x9o2uauVYKxjOelRF27DUbQ0_xQTQrXC68RopsuoZ1HA9g7nBSERkSLmQI8lsiRHt2dHOfW0hXOtmasWtFMQrM604byB2yq1N6cpJC_-H-nfAWfGPeawkI5Kcg-rnZ4fE3aeGLodhtzA3zpqqgCfi6S4rWF1d_z95SQPvAx_rhTnObUVCgiDnJ2FjNRwAAAAHwflN5AA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/sunset_mountain.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/starry_night.jpg"
)
PLAYLIST_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/starry_night.jpg"
STATS_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/sunset_mountain.jpg"
TELEGRAM_AUDIO_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
TELEGRAM_VIDEO_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
STREAM_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
SOUNCLOUD_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"
YOUTUBE_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )














