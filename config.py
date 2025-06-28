#  Copyright (c) 2025 AshokShau
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the TgMusicBot project. All rights reserved where applicable.


from os import getenv
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

"You can get these variables from my.telegram.org"
API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")

"You can get this variable from @BotFather"
TOKEN = getenv("TOKEN", "2096983652:AAHz41orhz9RrWscwg_WwSCp0_OhP-zLmDY")

"Pyrogram (Forks) String Session, min. add one string session"
STRING = getenv("STRING", "BQGJMTYALFX3dQvrOJlHh_mm12o2A-zJL3mH43MY8QkaXiTXd0uAIhdgA5kAZuqkPiRVDyaLHd6XCQDbllXGSsTu9C-yIIc-bmDDLVQ3ZekqCnchluPP6BHV1vKM6Hn4Pgph9tJ7mmdWumI2e_wpzbwloaEP4OAjIZoti1jF8_BpJPBCAZrQfLCglBpRltjiFaDh-lY8p95TPWFwdhyyDYkHCGNIbf3Rcs7VF1jIyprsExSczs9licjn1VUeWNcLbgS6sYzc7ZwrWFEsprJUjn_Y3rVr3Bj4uyDy55o2qNtn3Mb5xSU2bwY0gn3Kovc8mWOOjYI6d0zSr93ddH-JNjwNxxZxwgAAAAHSHPeVAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = getenv("STRING6", None)
STRING7 = getenv("STRING7", None)
STRING8 = getenv("STRING8", None)
STRING9 = getenv("STRING9", None)
STRING10 = getenv("STRING10", None)

SESSION_STRINGS = [
    STRING,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
    STRING6,
    STRING7,
    STRING8,
    STRING9,
    STRING10,
]

"Your Telegram User ID"
OWNER_ID = int(getenv("OWNER_ID", 1281282633))

"Channel/Group ID for logging; where logs will be sent"
LOGGER_ID = int(getenv("LOGGER_ID", "-1001735663878"))

"Your MongoDB URI; get it from https://cloud.mongodb.com"
MONGO_URI = getenv("MONGO_URI", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")

"Spotify dl get from @AshokShau"
API_URL = getenv("API_URL", "487064a94b42419987704fe395492701")
API_KEY = getenv("API_KEY", "ec6615520a9d47d7865ec1e08b39915b")

"Proxy URL for yt-dlp"
PROXY_URL = getenv("PROXY_URL", None)

"Default platform to search for songs; options: youtube, spotify, jiosaavn"
DEFAULT_SERVICE = getenv("DEFAULT_SERVICE", "youtube").lower()

"Directory for downloads and TDLib db"
DOWNLOADS_DIR = getenv("DOWNLOADS_DIR", "database/music")

"Support group and channel"
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/HeartBeat_Muzic")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HeartBeat_Offi")

"If true, allows to skip all updates received while the TDLib instance was not running."
IGNORE_BACKGROUND_UPDATES = (
    getenv("IGNORE_BACKGROUND_UPDATES", "True").lower() == "true"
)


def process_cookie_urls(env_value: Optional[str]) -> list[str]:
    """Parse COOKIES_URL environment variable"""
    if not env_value:
        return []
    urls = []
    for part in env_value.split(","):
        urls.extend(part.split())

    return [url.strip() for url in urls if url.strip()]


"BatBin urls to download cookies; more info https://github.com/AshokShau/TgMusicBot/blob/master/cookies/README.md"
COOKIES_URL: list[str] = process_cookie_urls(getenv("COOKIES_URL", "https://batbin.me/hitchel"))
