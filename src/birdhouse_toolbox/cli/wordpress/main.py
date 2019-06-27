import click

from .commands.authenticate import authenticate
from .commands.create_post import create_post


@click.group(name="wp")
def main():
    pass


main.add_command(authenticate)
main.add_command(create_post)
