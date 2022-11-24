from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base


class PreBase:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class TestTable(Base):
    __tablename__ = 'test_table'
    idid = Column(Integer)
    idi2d = Column(Integer)


def create_db(engine):
    Base.metadata.create_all(engine)
