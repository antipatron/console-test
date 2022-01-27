import sys
import click
import requests

__author__ = "antipatron"

@click.group()
@click.version_option("1.0")
def main():
    """
    Simple CLI for math basic operations
    """
    pass

@main.command(short_help='init the repo')
@click.option('--value', '-va', help='Valores numericos separados por coma', required=False, type=str)
def sum(value):
    """Retorna la suma de los valores numericos"""
    print(value)
    if (len(value)>0):
        click.echo('\n'.join(value))

@main.command()
@click.option('--query', '-q', prompt=True)
@click.option('--limit', '-l', prompt=True)
def search(query, limit):
    """This search and return results corresponding to the given query from Google Books"""
    url_format = 'https://www.googleapis.com/books/v1/volumes'
    query = "+".join(query.split())
    print(limit)

    query_params = {
        'q': query
    }

    response = requests.get(url_format, params=query_params)

    click.echo(response.json()['items']) 

@main.command()
@click.argument('id')
@click.option('--inverso', '-in', help='Do nothing', required=False)
def get(id):
    """This return a particular book from the given id on Google Books"""
    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
    click.echo(id)

    response = requests.get(url_format.format(id))

    click.echo(response.json())


if __name__ == "__main__":
    main()