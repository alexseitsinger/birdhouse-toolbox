import os
from io import open


def read_file(path):
    if not os.path.isfile(path):
        raise FileNotFoundError("The file does not exist. ({})".format(path))
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
