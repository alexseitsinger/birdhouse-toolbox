from ..make_url import make_url
from ..request import request
from ...settings import WORDPRESS_POSTS_URI, DEFAULT_REQUEST_TIMEOUT


def get_post_content(site_url, post_number=0):
    url = make_url(site_url, WORDPRESS_POSTS_URI)
    response = request("get", url)
    content = response[post_number]["content"]["rendered"]
    return content
