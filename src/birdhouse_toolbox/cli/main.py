import click

from .wordpress import (
    get_posts,
    get_post,
    add_post,
    authenticate,
)
from ..settings import DEFAULT_REQUEST_TIMEOUT


class Options(object):
    def __init__(self, url=None, timeout=None):
        self.url = url
        self.timeout = timeout


@click.group()
@click.option("--url")
@click.option("--timeout", default=DEFAULT_REQUEST_TIMEOUT, required=False)
@click.pass_context
def main(ctx, url, timeout):
    ctx.obj = Options(url, timeout)

# wordpress commands
main.add_command(get_post)
main.add_command(get_posts)
main.add_command(add_post)
main.add_command(authenticate)

# analytics commands


