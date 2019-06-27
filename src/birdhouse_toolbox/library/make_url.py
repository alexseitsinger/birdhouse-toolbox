import re

from ..settings import HTTP_SCHEMES


def make_url(url, suffix, *args):
    # remove any '://' from the start of the string.
    url = re.sub(r"^(:?\/+)", "", url)
    # remove any / from the end of the string.
    url = re.sub(r"(\/+)$", "", url)
    # if the url doesnt start with 'http://'' or 'https://' add 'https://'.
    if not url.startswith(HTTP_SCHEMES):
        url = "{}{}".format(HTTP_SCHEMES[1], url)
    # if the url doesn't end with the provided suffix, add it.
    if not url.endswith(suffix):
        url = "/".join([url, suffix])
    # if there are args also provided, add them to the end.
    url = "/".join([url] + list(args))
    return url
