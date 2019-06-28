from ..make_url import make_url
from ...settings import WORDPRESS_POSTS_URI
from ..request import request


def get_posts(site_url, page_number=1, per_page=100):
    url = make_url(site_url, WORDPRESS_POSTS_URI)
    params = {"per_page": per_page, "page": page_number}
    return request("get", url, params=params)
