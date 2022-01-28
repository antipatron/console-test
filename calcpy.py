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

@main.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('numbertype', default="INT",type=click.Choice(['int', 'float']))
@click.option('--numbers', '-n', help='Valores numericos separados por signo más (+)', required=True)
def sum(numbers, numbertype):
    """Retorna la suma de los valores numericos"""
    print(numbertype)
    try:
        values = numbers.split(',')
        print(values)
    except ValueError:
        pass

    sum = 0
    for i, value in enumerate(values):
        try:
            parseNumber(numbertype, value)
        except ValueError:
            values[i] = value
        else:
            values[i] = parseNumber(numbertype, value)
            sum+=values[i]
    
    click.echo(f"Suma:  {sum}")

def parseNumber(numberType, number):
    if numberType=="int":
        return int(number)
    elif numberType == "float":
        return float(number)
    else:
        return int(number)



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