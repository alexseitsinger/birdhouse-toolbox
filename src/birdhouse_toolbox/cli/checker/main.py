import click

from .commands.check import check_command


@click.group(name="ck")
def main():
    pass


main.add_command(check_command)
