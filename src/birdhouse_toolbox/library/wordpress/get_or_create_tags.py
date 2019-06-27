from ..request import request
from ...settings import WORDPRESS_TAGS_URI


def get_tag(name):
    return request("get", WORDPRESS_TAGS_URI)


def create_tag(name):
    return request("post", WORDPRESS_TAGS_URI, data={"name": name})


def get_or_create_tag(name):
    try:
        tag = get_tag(name)
    except RuntimeError:
        tag = create_tag(name)
    return tag


def get_or_create_tags(tags):
    return [get_or_create_tag(x) for x in tags]
