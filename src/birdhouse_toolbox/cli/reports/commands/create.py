import click

from ....library.reports.commands.create_report import create_report

EXCEPTIONS_EXPECTED = (RuntimeError, FileNotFoundError, AttributeError)


@click.command(name="create")
def create_report_command():
    try:
        report_file = create_report()
        click.secho("Created report successfully.", fg="green", bold=True)
        click.secho(report_file, fg="green")
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to create report.", fg="red", bold=True)
        click.secho(str(exc))
