import logging


# Database settings
DATABASE_FILENAME = "db.json"
DB_AUTOSAVE_INTERVAL = 10  # seconds


# Logging settings
LOG_FILENAME = "univerzal.log"
LOG_LEVEL = logging.INFO
LOG_FILEMODE = "w"
LOG_FORMAT = "%(asctime)s :: %(levelname)s :: %(message)s"
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"


# Module settings
LOADED_MODULES = [
    "debug",
    "unz-control",
    "unz-quit",
]

MODULE_CONFIG = {
    "debug": {
        "report-on-message": True
    },
    "unz-control": {
        "confirm-message": "ok"
    },
    "unz-quit": {
        "confirm-message": "ok"
    }
}
