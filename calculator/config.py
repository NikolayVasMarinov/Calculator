import os
import json

CONFIG_FILE = "db/window_config.json"


def load_geometry():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE) as f:
                config = json.load(f)
                return config.get("geometry", "500x400")

        except:
            return "500x400"

    return "500x400"


def save_geometry(geometry):
    config = {"geometry": geometry}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)