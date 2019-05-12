from ..make_request import make_request
from ..make_url import make_url
from ...settings import WORDPRESS_JWT_URL


def get_jwt(site_url, username, password):
    full_url = make_url(site_url, WORDPRESS_JWT_URL, "token")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "username": username,
        "password": password,
    }
    return make_request(
        method="post",
        url=full_url,
        headers=headers,
        data=data,
    )
