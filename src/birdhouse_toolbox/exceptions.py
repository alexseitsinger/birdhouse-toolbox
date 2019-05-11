class RequestMethodIncorrectException(Exception):
    pass


class RequestTimeoutException(Exception):
    pass


class RequestFailureException(Exception):
    pass


class ReadConfigException(Exception):
    pass


class ReadWordpressConfigException(Exception):
    pass


class ReadWordpressCredentialsConfigException(Exception):
    pass


class ReadWordpressJWTConfigException(Exception):
    pass
