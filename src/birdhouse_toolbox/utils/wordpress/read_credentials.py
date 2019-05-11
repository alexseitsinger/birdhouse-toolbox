import json
from json import JSONDecodeError
import os

from ..read_config import read_config
from ...exceptions import (
    ReadWordpressConfigException,
    ReadWordpressCredentialsConfigException,
)


def read_credentials(site_url, config_file_name=None):
    config = read_config(site_url, config_file_name)
    wordpress = config.get("wordpress", None)
    if wordpress is None:
        raise ReadWordpressConfigException(
            "No wordpress config for {}".format(site_url)
        )
    credentials = wordpress.get("credentials", None)
    if credentials is None:
        raise ReadWordpressCredentialsConfigException(
           "No wordpress credentials config for {}.".format(site_url)
        )
    return credentials
