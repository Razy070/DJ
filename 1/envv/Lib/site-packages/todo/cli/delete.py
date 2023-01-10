import click
from todo.todo import TodoMananger


@click.command()
@click.option('-nt', help='notebook name')
@click.option('-t', default=None, help='item title')
def cli(nt, t=None):
    todo = TodoMananger()

    if not t:
        todo.delete_notebook(nt)
        print '%s notebook deleted' % (nt,)

    else:
        todo.delete(nt, t)
        print '%s item from %s notebook deleted' % (t, nt,)
