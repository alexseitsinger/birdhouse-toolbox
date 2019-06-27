from ..read_credentials import read_credentials
from ..save_credentials import save_credentials
from ..get_jwt import get_jwt
from ..save_jwt import save_jwt


def authenticate(site_url, username=None, password=None):
    if username is None and password is None:
        credentials = read_credentials(site_url)
        username = credentials["username"]
        password = credentials["password"]
    else:
        save_credentials(site_url, username, password)
    save_jwt(site_url, get_jwt(site_url, username, password))
