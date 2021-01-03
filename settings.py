import logging
import os
import random

from misc import RandomRegexPersonality, RandomChoicePersonality


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
MEDIA_AUDIO_DIR = os.path.join(os.getcwd(), "media", "audio")

# Module settings
LOADED_MODULES = [
    "debug",
    "unz-control",
    "unz-quit",
    "unz-message",
    "unz-words",
    "unz-autoreply",
    "rps",
    "unz-audio",
]

MODULE_CONFIG = {
    "debug": {
        "report-on-message": True
    },
    "unz-autoreply": {
        "personalities": [
            RandomRegexPersonality(
                [
                    "univer(s|z)al",
                    "bot",
                    "discord",
                ],
                [
                    "Univerzal is a framework for discord bots!",
                    lambda: "Univerzal is univer{}al".format(
                        random.choice(["s", "z"])
                    )
                ]
            ),
            RandomChoicePersonality(
                [
                    "bot"
                ],
                [
                    "Beep boop."
                ],
                priority=1
            )
        ]
    }
}
