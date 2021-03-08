"""
constants, settings
"""
import os
import secrets
from pathlib import Path

from dotenv import load_dotenv

from .db import init_from_environment
from .karmic_restriction import init_default
from .karmic_triggers import (
    PLUS,
    PLUS_TRIGGERS,
    PLUS_EMOJI,
    PLUS_WORDS,
    MINUS,
    MINUS_TRIGGERS,
    MINUS_EMOJI,
)

app_dir: Path = Path(__file__).parent.parent.parent
load_dotenv(str(app_dir / '.env'))

TIME_TO_CANCEL_ACTIONS = 60
TIME_TO_REMOVE_TEMP_MESSAGES = 30

auto_restrict_config = init_default()
PROG_NAME = "KarmaBot"
PROG_DESC = (
    "This program is a Python 3+ script. The script launches a bot in Telegram,"
    " allowing change karma for chat members"
)
PROG_EP = "© bomzheg. License WTFPL."
DESC_BETA = "Run the program in beta test mode"
DESC_POLLING = "Run tg bot with polling. Default use WebHook"

BOT_TOKEN = os.getenv("KARMA_BOT_TOKEN")
secret_str = secrets.token_urlsafe(16)  # for webhook path

PRINT_LOG = "print.log"

BOMZHEG_ID = 46866565
BORNTOHACK_ID = 113196531
ENTERESSI_ID = 198896585
VADIM_ID = 109601
RUD_ID = 695207573
LET45FC_ID = 384612009
STUDENT_ID = 431590221
GLOBAL_ADMIN_ID = BOMZHEG_ID
SUPERUSERS = {GLOBAL_ADMIN_ID, BOMZHEG_ID, BORNTOHACK_ID, ENTERESSI_ID, VADIM_ID,
              RUD_ID, LET45FC_ID, STUDENT_ID}
LOG_CHAT_ID = -1001404337089
DUMP_CHAT_ID = -1001459777201  # ⚙️Testing Area >>> Python Scripts

DATE_FORMAT = '%d.%m.%Y'

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PORT = os.getenv("WEBHOOK_PORT", default=443)
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", default='/karmabot/')
WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}"

LISTEN_IP = os.getenv("LISTEN_IP", default='0.0.0.0')
LISTEN_PORT = int(os.getenv("LISTEN_PORT", default=3000))

db_config = init_from_environment(app_dir)

API_ID = os.getenv("API_ID", default=6)
API_HASH = os.getenv("API_HASH", default='eb06d4abfb49dc3eeb1aeb98ae0f581e')