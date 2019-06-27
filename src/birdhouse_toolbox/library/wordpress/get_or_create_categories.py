from slugify import slugify
import json

from ..request import request
from ...settings import WORDPRESS_CATEGORIES_URI
from ..make_url import make_url
from .get_authentication_header import get_authentication_header


def create_category(site_url, name):
    url = make_url(site_url, WORDPRESS_CATEGORIES_URI)
    data = {"name": name, "slug": slugify(name)}
    headers = get_authentication_header(site_url)
    try:
        return request("post", url, data=data, headers=headers)
    except RuntimeError as exc:
        msg = str(exc)
        data_str = "".join(msg.split("\n")[2:])
        data = json.loads(data_str)
        if data["code"] == "term_exists":
            raise RuntimeError("The term '{}' already exists as a tag.".format(name))
        raise exc


def get_category(site_url, name):
    slug = slugify(name)
    url = make_url(site_url, WORDPRESS_CATEGORIES_URI)
    response = request("get", url, params={"slug": slug})
    if len(response) > 1:
        raise RuntimeError("Found more than 1 category for slug '{}'.".format(slug))
    return response[0]


def get_or_create_category(site_url, name):
    cat = get_category(site_url, name)
    if cat is None:
        cat = create_category(site_url, name)
    return cat


def get_or_create_categories(site_url, categories):
    return [get_or_create_category(site_url, x) for x in categories]
