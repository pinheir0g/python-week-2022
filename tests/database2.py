from sqlmodel import create_engine
from tests import teste

engine = create_engine('sqlite:///berrlog2.db')
teste.SQLModel.metadata.create_all(engine)
