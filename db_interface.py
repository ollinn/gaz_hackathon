from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from constants import CONNECT_STRING, DIALECT, CLIENT_DIR
import models

if DIALECT == 'oracle':
    import cx_Oracle

    cx_Oracle.init_oracle_client(CLIENT_DIR)

engine = create_engine(CONNECT_STRING)
models.create_db(engine)
session = Session(engine)


def get_departments_tree():
    tree = dict()
    for department in session.query(models.Department):
        tree[department] = department.head_department
    return tree
