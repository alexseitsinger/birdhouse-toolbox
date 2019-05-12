WORDPRESS_URL_PREFIX = "wp-json"

WORDPRESS_POSTS_URL = "{}/wp/v2/posts".format(WORDPRESS_URL_PREFIX)

WORDPRESS_JWT_URL = "{}/jwt-auth/v1".format(WORDPRESS_URL_PREFIX)

DEFAULT_REQUEST_TIMEOUT = 10.0

DEFAULT_REQUEST_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

DEFAULT_CONFIG_FILE_NAME = "birdhouse_toolbox.json"

HTTP_SCHEMES = ("http://", "https://",)

HTTP_METHODS_ALLOWED = ("get", "post", "put", "delete", "options", "head",)
