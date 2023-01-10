import click
from todo.todo import TodoMananger


@click.command()
@click.option('-nt', default=None, help='notebook name')
def cli(nt=None):
    todo = TodoMananger()

    if not nt:
        appdata = todo.list_all()

        for notebook_name, items in appdata.items():
            _print_notebook(notebook_name, items)
            print '\n'

    else:
        appdata = todo.list(notebook=nt)
        _print_notebook(nt, appdata)


def _print_notebook(notebook_name, appdata):
    print 'Items from %s' % (notebook_name,)

    for todo_item in appdata:
        print todo_item['title']
