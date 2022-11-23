from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from constants import ENGINE_PATH_WIN_AUTH, CLIENT_DIR

Base = declarative_base()
engine = create_engine(ENGINE_PATH_WIN_AUTH)
