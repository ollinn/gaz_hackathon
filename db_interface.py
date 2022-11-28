import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from constants import CONNECT_STRING, DIALECT, CLIENT_DIR
import models

if DIALECT == 'oracle':
    import cx_Oracle

    cx_Oracle.init_oracle_client(CLIENT_DIR)

engine = create_engine(CONNECT_STRING)
# models.create_db(engine)
session = Session(engine)


def print_partners():
    for partner in session.query(models.Summary):
        print(partner)


print_partners()
