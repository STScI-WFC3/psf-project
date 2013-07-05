#! /usr/bin/env python

'''
This is the connection module for the psf database.
'''

import socket

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from ql_database_interface import loadConnection
from ql_database_interface import SETTINGS

if socket.gethostname() == SETTINGS['development_machine']:
    session, Base = loadConnection('sqlite:///../database/psf.db')

class PSFTable(Base):
    '''
    ORM for the psf table.
    '''
    __tablename__ = 'psf'
    id  = Column(Integer(11), primary_key=True)
    x_center = Column(Integer(4))
    y_center = Column(Integer(4))
    #sky = Column(Float())
    psf_array = Column(String())

    def __init__(self, x_center, y_center, psf_array):
        self.x_center = x_center
        self.y_center = y_center
        self.psf_array = psf_array

    def __repr__(self):
        print '{}, {}, {}'.format(self.x_center, self.y_center, self.psf_array)

## Drop and recreate the tables.
Base.metadata.drop_all()
Base.metadata.create_all() 