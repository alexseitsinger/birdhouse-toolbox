import os
import json
from json import JSONDecodeError

from ..save_config import save_config
from ...settings import DEFAULT_CONFIG_FILE_NAME


def save_credentials(
    site_url,
    username,
    password,
    config_file_name=DEFAULT_CONFIG_FILE_NAME
):
    payload = {"username": username, "password": password}
    save_config(site_url, "wordpress", {"credentials": payload}, config_file_name)
