from slugify import slugify

from ..request import request
from ...settings import WORDPRESS_TAGS_URI
from ..make_url import make_url
from .get_authentication_header import get_authentication_header


def create_tag(site_url, name):
    url = make_url(site_url, WORDPRESS_TAGS_URI)
    data = {"name": name, "slug": slugify(name)}
    headers = get_authentication_header(site_url)
    return request("post", url, data=data, headers=headers)


def get_tags(site_url):
    url = make_url(site_url, WORDPRESS_TAGS_URI)
    response = request("get", url)
    return response


def get_tag(site_url, key):
    if isinstance(key, str):
        key = slugify(key)
    for tag in get_tags(site_url):
        if isinstance(key, str) and tag["slug"] == key:
            return tag
        if isinstance(key, int) and tag["id"] == key:
            return tag


def get_or_create_tag(site_url, name):
    tag = get_tag(site_url, name)
    if tag is None:
        tag = create_tag(site_url, name)
    return tag


def get_or_create_tags(site_url, tags):
    return [get_or_create_tag(site_url, x) for x in tags]
