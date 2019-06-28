import click

from .commands.create import create


@click.group(name="rp")
def main():
    pass


main.add_command(create)
