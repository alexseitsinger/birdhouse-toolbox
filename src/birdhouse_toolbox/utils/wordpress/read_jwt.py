import json
from json import JSONDecodeError
import os

from ..read_config import read_config
from ...exceptions import (
    ReadWordpressJWTConfigException,
    ReadWordpressConfigException
)


def read_jwt(site_url, config_file_name=None):
    config = read_config(site_url, config_file_name)
    wordpress = config.get("wordpress", None)
    if wordpress is None:
        raise ReadWordpressConfigException(
            "No wordpress config for {}".format(site_url)
        )
    jwt = wordpress.get("jwt", None)
    if jwt is None:
        raise ReadWordpressJWTConfigException(
            "No wordpress JWT config for {}".format(site_url)
        )
    return jwt
