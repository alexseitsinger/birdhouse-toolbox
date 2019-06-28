import click

from .commands.create import create_report_command


@click.group(name="rp")
def main():
    pass


main.add_command(create_report_command)
