import click

from ....utils import make_request, make_url
from ....utils.wordpress import read_credentials
from ....settings import WORDPRESS_POSTS_URL


@click.command()
@click.pass_obj
def get_posts(options):
    headers = {}
    click.echo(make_request(
        method="get",
        url=make_url(options.url, WORDPRESS_POSTS_URL),
        headers=headers,
        timeout=options.timeout,
    ))
