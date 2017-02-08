#
#   Author  : Anjani Suresh Bhat
#   Date    : August 2016
#
#   This file is to create a class which maps to a database
#
#


import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Items(Base):
        """
        This calss is to create table in database
        Each attribute will be a column in the database
        """
        __tablename__ = 'items'

        id = Column(Integer, primary_key=True)
        name = Column(String(40))
        picture = Column(String(100))
        price = Column(String(40))
        type_item = Column(String(40))
        description = Column(String(200))
        brand_name = Column(String(30))

engine = create_engine('sqlite:///item_list.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()
'''
try:
    num_rows_deleted = session.query(Items).delete()
    session.commit()
except:
    session.rollback()
'''


Base.metadata.create_all(engine)
