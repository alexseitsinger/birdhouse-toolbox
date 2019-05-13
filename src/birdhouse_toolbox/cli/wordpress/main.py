import click

from .commands import (
    add_post,
    get_posts,
    get_post,
    authenticate,
)


@click.group(name="wordpress")
def main():
    pass


main.add_command(authenticate)
main.add_command(get_posts)
main.add_command(get_post)
main.add_command(add_post)
