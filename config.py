import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5266741503:AAH17F9W4MAZnqq6TPGqzKg4v43LZpQPYyo")
API_ID = int(os.environ.get("API_ID", 5026910))
API_HASH = os.environ.get("API_HASH", "16d35ae89273082f96d6e87013a5a260")
RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 4))  # NOTE Number of results to show, 4 is better
SUDO_CHATS_ID = list(set(int(x) for x in os.environ.get("SUDO_CHATS_ID", "-1001791208631 1346381156").split()))
DRIVE_NAME = list(set(x for x in os.environ.get("DRIVE_NAME", "Server-1,Server-2").split(",")))
DRIVE_ID = list(set(x for x in os.environ.get("DRIVE_ID", "1a-3JH0YimjBcrTEDPy3ZdrXm2vhKFREU 1O21xupr3T1Mp7krMpzgudz80FXvbrN9H").split()))
INDEX_URL = list(set(x for x in os.environ.get("INDEX_URL", "https://www1.thopdb.com/0:/Server-1/ https://www1.thopdb.com/0:/Server-2/").split()))
