import os
from slugify import slugify

from ..get_authentication_header import get_authentication_header
from ..format_as_html import format_as_html
from ..create_post_content import create_post_content
from ..get_or_create_tags import get_or_create_tags
from ..get_or_create_categories import get_or_create_categories
from ..create_featured_media import create_featured_media
from ...request import request
from ...make_url import make_url
from ...read_file import read_file
from ....settings import WORDPRESS_POSTS_URI


def create_post(site_url, title, content, status, tags, categories, media, timeout):
    if os.path.isfile(content):
        content = read_file(content)
        body_markup = format_as_html(content)
    else:
        body_markup = content

    rest_url = make_url(site_url, WORDPRESS_POSTS_URI)
    last_post = request("get", rest_url, timeout=timeout)[0]
    return request(
        "post",
        rest_url,
        timeout=timeout,
        headers=get_authentication_header(site_url),
        data={
            "slug": slugify(title),
            "status": status,
            "title": title,
            "content": create_post_content(site_url, body_markup),
            "tags": [x["id"] for x in get_or_create_tags(site_url, tags)],
            "categories": [
                x["id"] for x in get_or_create_categories(site_url, categories)
            ],
            # "featured_media": create_featured_media(site_url, media),
            "meta": last_post["meta"],
            "template": last_post["template"],
        },
    )
