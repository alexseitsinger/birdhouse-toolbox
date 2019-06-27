import os
import click

from ....library.wordpress.create_post import create_post as fn


@click.command(name="create")
@click.option("--title", required=True, help="The title of the post.")
@click.option("--content", required=True, help="The post content.")
@click.option(
    "--status",
    default="publish",
    required=False,
    help="May be either 'draft' or 'publish'.",
)
@click.option("--tag", multiple=True, required=False, help="The tags for the post.")
@click.option(
    "--category", multiple=True, required=False, help="The category of the post."
)
@click.pass_obj
def create_post(options, title, content, status, tag, category):
    try:
        response = fn(
            site_url=options.url,
            title=title,
            content=content,
            status=status,
            tags=tag,
            categories=category,
            timeout=options.timeout,
        )
        click.secho("Post creation succeeded.", fg="green", bold=True)
    except RuntimeError as exc:
        click.secho("Post creation failed.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
