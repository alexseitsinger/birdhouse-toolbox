from ..read_credentials import read_credentials
from ..save_credentials import save_credentials
from ..get_jwt import get_jwt
from ..save_jwt import save_jwt


def authenticate(url, username=None, password=None):
    if username is None and password is None:
        credentials = read_credentials(url)
        username = credentials["username"]
        password = credentials["password"]
    else:
        save_credentials(url, username, password)
    save_jwt(url, get_jwt(url, username, password))
