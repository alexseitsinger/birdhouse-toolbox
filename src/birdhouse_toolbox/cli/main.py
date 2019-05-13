import click

from .options import Options
from .wordpress import main as wordpress_main
from .analytics import main as analytics_main
from ..settings import DEFAULT_REQUEST_TIMEOUT


@click.group()
@click.option("--url")
@click.option("--timeout", default=DEFAULT_REQUEST_TIMEOUT, required=False)
@click.pass_context
def main(ctx, url, timeout):
    ctx.obj = Options(url, timeout)


main.add_command(wordpress_main)
main.add_command(analytics_main)


