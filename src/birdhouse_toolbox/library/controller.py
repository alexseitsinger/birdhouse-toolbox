import os
import json


class BirdhouseToolbox(object):
    config_file_name = "birdhouse-toolbox.json"
    config_file_path = None
    config = None
    config_key = None
    site_url = None

    def __init__(self, site_url):
        self.site_url = site_url
        self.set_config()

    def set_config(self):
        if self.config is None:
            home = os.path.abspath(os.path.expanduser("~"))
            self.config_file_path = os.path.join(home, self.config_file_name)
            with open(self.config_file_path, "r") as f:
                data = json.loads(f.read())
                site_data = data[self.site_url]
                if self.config_key is None:
                    self.config = site_data
                else:
                    self.config = site_data[self.config_key]
