from ..request import request
from ..make_url import make_url
from ...settings import WORDPRESS_JWT_URI


def get_jwt(site_url, username, password):
    url = make_url(site_url, WORDPRESS_JWT_URI, "token")
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"username": username, "password": password}
    return request("post", url, headers=headers, data=data)
