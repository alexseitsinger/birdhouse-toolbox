import click

from ....library.checker import check

EXCEPTIONS_EXPECTED = (RuntimeError, AttributeError, FileNotFoundError, AssertionError)


@click.command()
@click.argument("status_code", default=200)
@click.argument("follow", default=True)
@click.argument("local_only", default=True)
@click.pass_obj
def check_command(obj, status_code, follow, local_only):
    try:
        results = check(obj.url, status_code, follow, local_only)
        click.secho(results, fg="green")
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to check anchors.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
