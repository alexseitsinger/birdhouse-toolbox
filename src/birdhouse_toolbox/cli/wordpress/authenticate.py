import click

from ...utils.wordpress import (
    save_credentials,
    get_jwt,
    save_jwt,
    read_credentials
)


@click.command()
@click.option("--username", default=None, required=False)
@click.option("--password", default=None, required=False)
@click.pass_obj
def authenticate(options, username, password):
    url = options.url
    if username is None and password is None:
        credentials = read_credentials(url)
        username = credentials["username"]
        password = credentials["password"]
    else:
        save_credentials(url, username, password)
    save_jwt(url, get_jwt(url, username, password))
