import os
import json
import logging

import settings as stg
from unz_modules.base_module import UnzBaseModule


def load_or_create():
    filepath = os.path.join(os.getcwd(), stg.DATABASE_FILENAME)
    if os.path.exists(filepath):
        with open(filepath) as f:
            return json.load(f)
    else:
        db = {
            "unz_global": {}
        }
        return db


def save(database, loaded_modules):
    database["unz_global"] = UnzBaseModule.global_data
    for module in loaded_modules:
        database[module.name] = module.get_db()
    filepath = os.path.join(os.getcwd(), stg.DATABASE_FILENAME)
    logging.debug(f"Saving database at filepath {filepath}")
    with open(filepath, "w") as f:
        json.dump(database, f)
