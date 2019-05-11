import click
from slugify import slugify

from ...utils import (
    make_request,
    make_url,
)
from ...utils.wordpress import (
    create_post_content,
    read_credentials,
    get_authentication_header,
)
from ...settings import POSTS_URL


@click.command()
@click.option("--title")
@click.option("--markup")
@click.option("--status", default="publish")
@click.pass_obj
def add_post(options, title, markup, status):
    site_url = options.url
    timeout = options.timeout
    rest_url = make_url(site_url, POSTS_URL)
    last_post = make_request(method="get", url=rest_url, timeout=timeout)[0]
    click.echo(make_request(
        method="post",
        url=rest_url,
        timeout=timeout,
        headers=get_authentication_header(site_url),
        data={
            #"date": "",
            #"date_gmt", "",
            "slug": slugify(title),
            "status": status,
            #"password": None,
            "title": title,
            "content": create_post_content(site_url, markup),
            #"author": 3,
            #"excerpt": last_post["excerpt"],
            #"featured_media": last_post["featured_media"],
            #"comment_status": last_post["comment_status"],
            #"ping_status": last_post["ping_status"],
            #"format": last_post["format"],
            "meta": last_post["meta"],
            #"sticky": last_post["sticky"],
            "template": last_post["template"],
        },
    ))
