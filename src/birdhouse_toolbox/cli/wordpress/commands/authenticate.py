import click


from ....library.wordpress.commands.authenticate import authenticate as fn


@click.command(name="auth")
@click.option("--username", "-u", help="The username to log in with.")
@click.option("--password", "-p", help="The password to log in with.")
@click.pass_obj
def authenticate(options, username, password):
    try:
        fn(options.url, username, password)
        click.secho("Authentication succeeded.", fg="green", bold=True)
    except (AttributeError, RuntimeError) as exc:
        click.secho("Authentication failed.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
