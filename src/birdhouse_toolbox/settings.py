WORDPRESS_API_URI = "wp-json/wp/v2"

WORDPRESS_POSTS_URI = "{}/posts".format(WORDPRESS_API_URI)

WORDPRESS_TAGS_URI = "{}/tags".format(WORDPRESS_API_URI)

WORDPRESS_CATEGORIES_URI = "{}/categories".format(WORDPRESS_API_URI)

WORDPRESS_MEDIA_URI = "{}/media".format(WORDPRESS_API_URI)

WORDPRESS_JWT_URI = "wp-json/jwt-auth/v1"

DEFAULT_REQUEST_TIMEOUT = 10.0

DEFAULT_REQUEST_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

DEFAULT_CONFIG_FILE_NAME = "birdhouse-toolbox.json"

HTTP_SCHEMES = ("http://", "https://")

HTTP_METHODS_ALLOWED = ("get", "post", "put", "delete", "options", "head")

CONTENT_TYPES_ALLOWED = {
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
}
