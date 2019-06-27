from .read_jwt import read_jwt


def get_authentication_header(site_url):
    jwt = read_jwt(site_url)
    token = jwt.get("token", None)
    if token is None:
        return {}
    return {"Authorization": "Bearer " + token}
