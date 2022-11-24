from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from constants import CONNECT_STRING
from models import create_db

engine = create_engine(CONNECT_STRING)
create_db(engine)
session = Session(engine)
