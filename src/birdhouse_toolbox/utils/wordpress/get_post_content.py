from ..make_url import make_url
from ..make_request import make_request
from ...settings import POSTS_URL, DEFAULT_TIMEOUT


def get_post_content(site_url, post_number=0):
    rest_url = make_url(site_url, POSTS_URL)
    response = make_request("get", url=rest_url, timeout=DEFAULT_TIMEOUT)
    return response[post_number]["content"]["rendered"]
