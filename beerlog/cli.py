import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Beer Managment Application")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """
    Adds a new beer to database.
    :param name: Beer's name.
    :param style: Beer's style.
    :return: Add beer to database.
    """
    if add_beer_to_database(name, style, flavor, image, cost):
        print("\033[34mBeer added to database\033[m")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """
    list beers in database.
    :param style: Beer's style.
    :return: List all beers of the style.
    """
    beers = get_beers_from_database()
    table = Table(title="\033[34mBEERLOG\033[m :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d-%T")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
