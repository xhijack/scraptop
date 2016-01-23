from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_tokopedia_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class ProductTokopedia(DeclarativeBase):
    __tablename__ = 'product_tokopedia'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, unique=True)
    title = Column(String(300))
    price = Column(Float)
    seller = Column(String(300))
    link_url = Column(String(300))
    location = Column(String(300))
    image_url = Column(String(300))


