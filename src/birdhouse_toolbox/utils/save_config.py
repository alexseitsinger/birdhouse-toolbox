import os
import json
from json import JSONDecodeError

from ..settings import DEFAULT_CONFIG_FILE_NAME


def save_config(
    site_url,
    key,
    value,
    config_file_name=DEFAULT_CONFIG_FILE_NAME
):
    config_file = os.path.join(os.path.expanduser("~"), config_file_name)
    encoding = "utf-8"
    data = {}
    # Get the existing data for the site.
    if os.path.exists(config_file):
        with open(config_file, "r", encoding=encoding) as old_file:
            try:
                data = json.loads(old_file.read())
            except JSONDecodeError:
                data = {}
    # Update the data with our passed in value.
    with open(config_file, "w", encoding=encoding) as new_file:
        # get the data for the site.
        entry = data.get(site_url, {})
        # update the data using the new value
        entry.update({key: value})
        # set the data back into the original data.
        data[site_url] = entry
        # write the file.
        new_file.write(json.dumps(data))

