#! /usr/bin/env python

'''
This is the connection module for the psf database.
'''

from settings import SETTINGS

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from ql_database_interface import loadConnection


session, Base = loadConnection(SETTINGS['psf_connection_string'])

class PSFTable(Base):
    '''
    ORM for the psf table.
    '''
    __tablename__ = 'psf'
    id  = Column(Integer(11), primary_key=True)
    filename = Column(String())
    psf_x_center = Column(Integer(4))
    psf_y_center = Column(Integer(4))
    model_x_center = Column(Float(8))
    model_y_center = Column(Float(8))
    psf_flux = Column(Integer(12))
    sky = Column(Float(12))
    psf = Column(String())
    model_fraction = Column(String())

    def __init__(self, psf_dict):
        self.filename = psf_dict['filename']
        self.psf_x_center = psf_dict['psf_x_center']
        self.psf_y_center = psf_dict['psf_y_center']
        self.model_x_center = psf_dict['model_x_center']
        self.model_y_center = psf_dict['model_y_center']
        self.psf_flux = psf_dict['psf_flux']
        self.sky = psf_dict['sky']
        self.model_fraction = psf_dict['psf']
        self.model_fraction = psf_dict['model_fraction']

    def __repr__(self):
        print '{}, {}, {}'.format(self.x_center, self.y_center, self.psf_array)

## Drop and recreate the tables.
Base.metadata.drop_all()
Base.metadata.create_all() 