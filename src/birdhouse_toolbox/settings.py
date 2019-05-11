WORDPRESS_URL = "wp-json"

POSTS_URL = "{}/wp/v2/posts".format(WORDPRESS_URL)

JWT_URL = "{}/jwt-auth/v1".format(WORDPRESS_URL)

DEFAULT_TIMEOUT = 10.0

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

HTTP_SCHEMES = ("http://", "https://",)

DEFAULT_CONFIG_FILE_NAME = "birdhouse_toolbox.json"

HTTP_METHODS_ALLOWED = (
    "get", "post", "put", "delete", "options", "head",
)
