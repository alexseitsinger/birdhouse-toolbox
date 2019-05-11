import click

from ...utils.wordpress import (
    make_request,
    make_url,
    read_credentials
)
from ...settings import POSTS_URL


@click.command()
@click.option("--id", required=True, help="The ID of the post")
@click.pass_obj
def get_post(options, id):
    headers = {}`
    click.echo(make_request(
        method="get",
        url=make_url(options.url, POSTS_URL, id),
        timeout=options.timeout,
        headers=headers,
    ))
