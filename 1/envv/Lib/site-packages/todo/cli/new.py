import click
from todo.todo import TodoMananger


@click.command()
@click.option('-nt', default=None, help='notebook name')
@click.option('-t', help='the name of the todo item')
@click.option('-c', help='notify cron of the todo item, eg: 0 12 * * *')
def cli(t, nt=None, c=None):
    todo = TodoMananger()
    todo.add_item(t, notebook=nt, cron=c)
