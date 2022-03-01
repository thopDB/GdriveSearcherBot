import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5266741503:AAH17F9W4MAZnqq6TPGqzKg4v43LZpQPYyo")
API_ID = int(os.environ.get("API_ID", 5026910))
API_HASH = os.environ.get("API_HASH", "16d35ae89273082f96d6e87013a5a260")
RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 4))  # NOTE Number of results to show, 4 is better
SUDO_CHATS_ID = list(set(int(x) for x in os.environ.get("SUDO_CHATS_ID", "-1001791208631").split()))
DRIVE_NAME = list(set(x for x in os.environ.get("DRIVE_NAME", "Root").split(",")))
DRIVE_ID = list(set(x for x in os.environ.get("DRIVE_ID", "0AEtL-TilLpk8Uk9PVA").split()))
INDEX_URL = list(set(x for x in os.environ.get("INDEX_URL", "https://www1.thopdb.com/0:/").split()))
