import json
from slugify import slugify

from ..request import request
from ...settings import WORDPRESS_TAGS_URI
from ..make_url import make_url
from .get_authentication_header import get_authentication_header


def create_tag(site_url, name):
    url = make_url(site_url, WORDPRESS_TAGS_URI)
    data = {"name": name, "slug": slugify(name)}
    headers = get_authentication_header(site_url)
    try:
        return request("post", url, data=data, headers=headers)
    except RuntimeError as exc:
        msg = str(exc)
        data_str = "".join(msg.split("\n")[2:])
        data = json.loads(data_str)
        if data["code"] == "term_exists":
            raise RuntimeError(
                "The term '{}' already exists as a category.".format(name)
            )
        raise exc


def get_tag(site_url, name):
    slug = slugify(name)
    url = make_url(site_url, WORDPRESS_TAGS_URI)
    response = request("get", url, params={"slug": slug})
    if len(response) > 1:
        raise RuntimeError("Found more than 1 tag for slug '{}'.".format(slug))
    return response[0]


def get_or_create_tag(site_url, name):
    tag = get_tag(site_url, name)
    if tag is None:
        tag = create_tag(site_url, name)
    return tag


def get_or_create_tags(site_url, tags):
    return [get_or_create_tag(site_url, x) for x in tags]
