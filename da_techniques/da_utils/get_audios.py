import json
import sys


def get_audios(path):
    if path.endswith(".json"):
        with open(path, "r") as f:
            audios = json.load(f)
    else:
        print("Invalid file")
        sys.exit(1)
    return audios
