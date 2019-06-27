import os
import json
from json import JSONDecodeError

from ..read_config import read_config
from ...settings import DEFAULT_CONFIG_FILE_NAME

MISSING_CONFIG_MESSAGE = "No wordpress config for {site_url}"
MISSING_CREDENTIALS_MESSAGE = "No wordpress credentials for {site_url}"


def read_credentials(site_url, config_file_name=DEFAULT_CONFIG_FILE_NAME):
    config = read_config(site_url, config_file_name)
    wordpress = config.get("wordpress", None)
    if wordpress is None:
        raise AttributeError(MISSING_CONFIG_MESSAGE.format(site_url=site_url))
    credentials = wordpress.get("credentials", None)
    if credentials is None:
        raise AttributeError(MISSING_CREDENTIALS_MESSAGE.format(site_url=site_url))
    return credentials
