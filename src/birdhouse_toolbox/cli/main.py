import click

from .options import Options
from .wordpress.main import main as wordpress_group
from .reports.main import main as reports_group
from ..settings import DEFAULT_REQUEST_TIMEOUT


@click.group()
@click.option("--url", "-u", required=True)
@click.option("--timeout", "-t", required=False, default=DEFAULT_REQUEST_TIMEOUT)
@click.pass_context
def main(ctx, url, timeout):
    ctx.obj = Options(url, timeout)


main.add_command(wordpress_group)
main.add_command(reports_group)
