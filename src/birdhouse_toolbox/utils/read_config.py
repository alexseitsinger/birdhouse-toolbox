import json
from json import JSONDecodeError
import os

from ..settings import DEFAULT_CONFIG_FILE_NAME
from ..exceptions import ReadConfigException


def read_config(site_url, config_file_name=DEFAULT_CONFIG_FILE_NAME):
    path = os.path.join(os.path.expanduser("~"), config_file_name)
    if not os.path.isfile(path):
        raise ReadConfigException("Config file not found.")
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.loads(f.read())
        except JSONDecodeError:
            data = {}
    if site_url not in data:
        raise ReadConfigException("There is not config for {}".format(site_url))
    return data[site_url]

