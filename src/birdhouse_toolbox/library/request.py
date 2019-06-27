import requests
import json

from ..settings import (
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_REQUEST_HEADERS,
    HTTP_METHODS_ALLOWED,
)

INVALID_METHOD_MESSAGE = "Method must be one of: {}".format(
    ", ".join(list(HTTP_METHODS_ALLOWED))
)
BAD_REQUEST_MESSAGE = "{status_code}: {url}\n\n{message}"
REQUEST_TIMEOUT_MESSAGE = "{url} timed out after {timeout} seconds"


def request(
    method, url, params={}, data={}, headers={}, timeout=DEFAULT_REQUEST_TIMEOUT
):
    method = method.lower()
    try:
        fn = getattr(requests, method)
    except AttributeError:
        raise RuntimeError(INVALID_METHOD_MESSAGE)

    final_headers = {}
    final_headers.update(DEFAULT_REQUEST_HEADERS)
    final_headers.update(headers)

    try:
        if method in ("get", "options", "head", "delete"):
            response = fn(url, params=params, headers=final_headers, timeout=timeout)

        elif method in ("post", "patch", "put"):
            current_content_type = final_headers["Content-Type"]
            if current_content_type == "application/json":
                data = json.dumps(data)

            response = fn(
                url, params=params, data=data, headers=final_headers, timeout=timeout
            )

        else:
            raise RuntimeError(INVALID_METHOD_MESSAGE)

        status_code = response.status_code
        if not str(status_code).startswith("2"):
            raise RuntimeError(
                BAD_REQUEST_MESSAGE.format(
                    status_code=status_code, url=url, message=response.text
                )
            )

        return response.json()

    except requests.ConnectionError:
        raise RuntimeError(REQUEST_TIMEOUT_MESSAGE.format(url=url, timeout=timeout))
