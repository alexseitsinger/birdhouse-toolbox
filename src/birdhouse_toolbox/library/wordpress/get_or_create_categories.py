from slugify import slugify

from ..request import request
from ...settings import WORDPRESS_CATEGORIES_URI
from ..make_url import make_url
from .get_authentication_header import get_authentication_header


def create_category(site_url, name):
    url = make_url(site_url, WORDPRESS_CATEGORIES_URI)
    data = {"name": name, "slug": slugify(name)}
    headers = get_authentication_header(site_url)
    return request("post", url, data=data, headers=headers)


def get_categories(site_url):
    url = make_url(site_url, WORDPRESS_CATEGORIES_URI)
    return request("get", url)


def get_category(site_url, key):
    if isinstance(key, str):
        key = slugify(key)
    cats = get_categories(site_url)
    for cat in cats:
        if isinstance(key, str):
            if cat["slug"] == key:
                return cat
        if isinstance(key, int):
            if cat["id"] == key:
                return cat


def get_or_create_category(site_url, name):
    cat = get_category(site_url, name)
    if cat is None:
        cat = create_category(site_url, name)
    return cat


def get_or_create_categories(site_url, categories):
    return [get_or_create_category(site_url, x) for x in categories]
