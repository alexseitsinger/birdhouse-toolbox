import os
import json
from json import JSONDecodeError

from ..save_config import save_config
from ...settings import DEFAULT_CONFIG_FILE_NAME


def save_jwt(site_url, payload, config_file_name=DEFAULT_CONFIG_FILE_NAME):
    save_config(site_url, "wordpress", {"jwt": payload}, config_file_name)
