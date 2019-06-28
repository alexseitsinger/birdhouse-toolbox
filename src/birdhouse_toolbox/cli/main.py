import click

from .options import Options
from .wordpress.main import main as wordpress_group
from .analytics.main import main as analytics_group
from .reports.main import main as reports_group
from ..settings import DEFAULT_REQUEST_TIMEOUT


@click.group()
@click.option("--url")
@click.option("--timeout", default=DEFAULT_REQUEST_TIMEOUT, required=False)
@click.pass_context
def main(ctx, url, timeout):
    ctx.obj = Options(url, timeout)


main.add_command(wordpress_group)
main.add_command(analytics_group)
main.add_command(reports_group)
