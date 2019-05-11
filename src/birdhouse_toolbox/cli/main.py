import click

from .wordpress import (
    get_posts,
    get_post,
    add_post,
    authenticate,
)
from .analytics import (
    #...
)
from .options import Options
from ..settings import DEFAULT_TIMEOUT


@click.group()
@click.option("--url")
@click.option("--timeout", default=DEFAULT_TIMEOUT, required=False)
@click.pass_context
def main(ctx, url, timeout):
    ctx.obj = Options(url, timeout)

# wordpress commands
main.add_command(get_post)
main.add_command(get_posts)
main.add_command(add_post)
main.add_command(authenticate)

# analytics commands


