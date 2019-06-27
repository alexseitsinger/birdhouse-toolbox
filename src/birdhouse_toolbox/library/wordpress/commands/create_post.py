import os
from slugify import slugify

from ..get_authentication_header import get_authentication_header
from ..format_as_html import format_as_html
from ..create_post_content import create_post_content
from ..get_or_create_tags import get_or_create_tags
from ...request import request
from ...make_url import make_url
from ...read_file import read_file
from ....settings import WORDPRESS_POSTS_URI


def create_post(site_url, title, content, status, tags, categories, timeout):
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
            # "date
            # "date_gmt", "",
            "slug": slugify(title),
            "status": status,
            # "password": None,
            "title": title,
            "content": create_post_content(site_url, body_markup),
            "tags": get_or_create_tags(tags),
            # "author": 3,
            # "excerpt": last_post["excerpt"],
            # "featured_media": last_post["featured_media"],
            # "comment_status": last_post["comment_status"],
            # "ping_status": last_post["ping_status"],
            # "format": last_post["format"],
            "meta": last_post["meta"],
            # "sticky": last_post["sticky"],
            "template": last_post["template"],
        },
    )
