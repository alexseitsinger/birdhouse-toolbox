import requests
import json

from ..settings import (
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_REQUEST_HEADERS,
    HTTP_METHODS_ALLOWED,
)
from ..exceptions import (
    RequestMethodIncorrectException,
    RequestTimeoutException,
    RequestFailureException,
)


def make_request(
    method,
    url,
    params={},
    data={},
    headers={},
    timeout=DEFAULT_REQUEST_TIMEOUT,
):
    # get the request method to use.
    method = method.lower()
    try:
        fn = getattr(requests, method)
    except AttributeError:
        raise RequestMethodIncorrectException(
            "Method must be one of: {}".format(
                ", ".join(list(HTTP_METHODS_ALLOWED))
            )
        )
    # Create a dictionary of the final headers to use.
    final_headers = {}
    final_headers.update(DEFAULT_REQUEST_HEADERS)
    final_headers.update(headers)
    # Try to make a successful request...
    try:
        # If its a "get" method, dont append data to it. Only params.
        if method in ("get", "options", "head",):
            response = fn(
                url,
                params=params,
                headers=final_headers,
                timeout=timeout,
            )
        else:
            # Otherwise, attempt to encode the data if its supposed to be JSON.
            current_content_type = final_headers["Content-Type"]
            json_content_type = "application/json"
            if current_content_type == json_content_type:
                data = json.dumps(data)
            response = fn(
                url,
                params=params,
                data=data,
                headers=final_headers,
                timeout=timeout,
            )
        status_code = response.status_code
        content = response.json()
        if not str(status_code).startswith("2"):
            raise RequestFailureException(
                "{}: {} - {}".format(url, status_code, content["message"])
            )
        return content
    except requests.ConnectionError:
        raise RequestTimeoutException(
            "{}: Timed out after {} seconds.".format(url, timeout)
            )
