import os
import json
from json import JSONDecodeError

from ..read_config import read_config
from ...settings import DEFAULT_CONFIG_FILE_NAME

MISSING_CONFIG_MESSAGE = "No wordpress config for {site_url}"
MISSING_JWT_MESSAGE = "No wordpress jwt for {site_url}"


def read_jwt(site_url, config_file_name=DEFAULT_CONFIG_FILE_NAME):
    config = read_config(site_url, config_file_name)
    wordpress = config.get("wordpress", None)
    if wordpress is None:
        raise AttributeError(MISSING_CONFIG_MESSAGE.format(site_url=site_url))
    jwt = wordpress.get("jwt", None)
    if jwt is None:
        raise AttributeError(MISSING_JWT_MESSAGE.format(site_url=site_url))
    return jwt
