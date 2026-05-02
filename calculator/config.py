import os
import json
from textwrap import indent

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

def load_state():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE) as f:
                config = json.load(f)
                return config.get("state", "normal")

        except:
            return "normal"

    return "normal"

def save_geometry(geometry):
    config = load_config()
    config["geometry"] = geometry
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def save_state(state):
    config = load_config()
    config["state"] = state
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}