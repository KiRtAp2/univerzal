import logging
import os


# Database settings
DATABASE_FILENAME = "db.json"
DB_AUTOSAVE_INTERVAL = 10  # seconds


# Logging settings
LOG_FILENAME = "univerzal.log"
LOG_LEVEL = logging.INFO
LOG_FILEMODE = "w"
LOG_FORMAT = "%(asctime)s :: %(levelname)s :: %(message)s"
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"

# Media storage settings
MEDIA_FILES_DIR = os.path.join(os.getcwd(), "media", "files")
MEDIA_IMAGES_DIR = os.path.join(os.getcwd(), "media", "images")

# Module settings
LOADED_MODULES = [
    "debug",
    "unz-control",
    "unz-quit",
    "unz-message",
    "unz-words",
]

MODULE_CONFIG = {
    "debug": {
        "report-on-message": True
    },
}
