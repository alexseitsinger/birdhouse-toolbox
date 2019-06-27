import os

from ..request import request
from ..make_url import make_url
from ...settings import WORDPRESS_MEDIA_URI, CONTENT_TYPES_ALLOWED
from .get_authentication_header import get_authentication_header

INVALID_CONTENT_TYPE_MESSAGE = "Image must be one of {}"


def create_featured_media(site_url, file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Media file not found.")
    file_name = os.path.basename(file_path)
    ext = file_name.split(".")[-1]
    if ext not in CONTENT_TYPES_ALLOWED:
        raise RuntimeError(
            INVALID_CONTENT_TYPE_MESSAGE.format(", ".join(CONTENT_TYPES_ALLOWED.keys()))
        )
    headers = get_authentication_header(site_url)
    headers.update(
        {
            "Cache-Control": "no-cache",
            "Content-Disposition": "attachment; filename={}".format(file_name),
            "Content-Type": CONTENT_TYPES_ALLOWED[ext],
        }
    )
    url = make_url(site_url, WORDPRESS_MEDIA_URI)
    with open(file_path, "rb") as f:
        return request("post", url, data=f, headers=headers)
