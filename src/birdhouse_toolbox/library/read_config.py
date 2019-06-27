import os
import json
from json import JSONDecodeError

from .read_file import read_file
from ..settings import DEFAULT_CONFIG_FILE_NAME


def read_config(site_url, config_file_name=DEFAULT_CONFIG_FILE_NAME):
    config_file_path = os.path.join(os.path.expanduser("~"), config_file_name)
    if not os.path.exists(config_file_path):
        with open(config_file_path, "w") as f:
            f.write("{}")
    try:
        data = json.loads(read_file(config_file_path))
    except JSONDecodeError:
        data = {}
    if site_url not in data:
        raise AttributeError("There is no config for {}.".format(site_url))
    return data[site_url]
