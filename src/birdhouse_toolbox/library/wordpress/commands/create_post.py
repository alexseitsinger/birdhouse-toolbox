import os
from slugify import slugify

from ..get_authentication_header import get_authentication_header
from ..create_post_content import create_post_content
from ..get_or_create_tags import get_or_create_tags
from ..get_or_create_categories import get_or_create_categories
from ..create_featured_media import create_featured_media
from ...request import request
from ...make_url import make_url
from ...read_file import read_file
from ....settings import WORDPRESS_POSTS_URI

# TODO: Instead of using last post, allow getting a post by ID or date, instead.

# TODO: We only want to copy published posts, so we should also check for "Draft"
# status, before choosing a post to duplicate.

# TODO: Update form shortcode insertion.


def create_post(site_url, title, content, status, tags, categories, media, timeout):
    html_markup = content
    if os.path.isfile(content) and content.endswith(".html"):
        html_markup = read_file(content)
    url = make_url(site_url, WORDPRESS_POSTS_URI)
    last_post = request("get", url, timeout=timeout)[0]
    featured_media = None
    if media is not None:
        featured_media = create_featured_media(site_url, media)["id"]
    return request(
        "post",
        url,
        timeout=timeout,
        headers=get_authentication_header(site_url),
        data={
            "slug": slugify(title),
            "status": status,
            "title": title,
            "content": create_post_content(site_url, html_markup),
            "tags": [x["id"] for x in get_or_create_tags(site_url, tags)],
            "categories": [
                x["id"] for x in get_or_create_categories(site_url, categories)
            ],
            "featured_media": featured_media,
            "meta": last_post["meta"],
            "template": last_post["template"],
        },
    )
