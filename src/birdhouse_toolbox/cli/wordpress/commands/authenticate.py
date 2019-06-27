import click


from ....library.wordpress.commands.authenticate import authenticate as fn


@click.command(name="auth")
@click.option("--username", "-u")
@click.option("--password", "-p")
@click.pass_obj
def authenticate(options, username, password):
    try:
        fn(options.url, username, password)
        click.secho("Authentication succeeded.", fg="green", bold=True)
    except (AttributeError, RuntimeError) as exc:
        click.secho("Authentication failed.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
