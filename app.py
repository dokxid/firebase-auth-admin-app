import click
import os
import firebase_admin as fire
from firebase_admin import credentials, auth
from dotenv import load_dotenv
from rich import print, inspect


load_dotenv('.env')
cred = credentials.Certificate(os.getenv("SECRET_PATH"))
fire.initialize_app(cred)


def list_users():
  list_users: auth.ListUsersPage = auth.list_users()
  q = list_users.users
  print('Successfully fetched user data:')
  for user in q:
      inspect(user, title=user.uid)

@click.group()
def cli():
    pass

@cli.command(help="list all user objects.")
def list():
    list_users()


@cli.command(help="set a field in user object")
def update():

    # uid selection
    list_users()
    uid = click.prompt("enter an uid", type=click.STRING)
    click.echo("selected user: ")
    u = auth.get_user(uid)
    inspect(u, title=u.uid)
    if click.confirm(f"proceed?"):
        click.echo(f"proceeding,,,")
    else:
        click.echo("aborted,,,")
        return

    # values to edit
    field = click.prompt("enter a claim field to edit", type=click.STRING, default="role")
    if field == "custom_claims":
        v1 = click.prompt("enter json value 1", type=click.STRING, default="role") 
        v2 = click.prompt("enter json value 2", type=click.STRING, default="privileged")
        value = {v1: v2}
    else:
        value = click.prompt("enter value", type=click.STRING, default="role") 
    d = {field: value}
    print(d)
    if click.confirm(f"proceed?"):
        auth.update_user(uid, **d)
        click.echo(f"{uid} successfully changed!")
    else:
        click.echo("aborted!")
        return


if __name__ == "__main__":
    cli()