from typing import List
from sqlmodel import select
from beerlog.database import get_session
from beerlog.models import Beer


def add_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int,
) -> bool:
    with get_session() as session:
        beer = Beer(
            name=name, style=style, flavor=flavor, image=image, cost=cost
        )
        session.add(beer)  # INSERT INTO beer VALUES (...)
        session.commit()
    return True


def get_beers_from_database() -> List[Beer]:
    """

    :rtype: object
    """
    with get_session() as session:
        sql = select(Beer)  # select * from beer;
        return list(session.exec(sql))
