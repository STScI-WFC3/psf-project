#! /usr/bin/env python

'''
Contains all the SQLAlchemy database ORM definitions.
'''

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

def loadConnection(connection_string):
    '''
    Create and engine using an engine string. Declare a base and 
    metadata. Load the session and return a session object.
    '''
    engine = create_engine(connection_string, echo=True)
    Base = declarative_base(engine)
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, Base

#----------------------------------------------------------------------------
# Define all the SQLAlchemy ORM bindings
#----------------------------------------------------------------------------

session, Base = loadConnection('sqlite:////grp/hst/wfc3a/Database/ql.db')


class Master(Base):
    '''
    ORM for the master table.
    '''
    __tablename__ = 'master'
    __table_args__ = {'autoload':True}


class UVISFLT0(Base):
    '''
    ORM for the uvis_flt_0 table.
    '''
    __tablename__ = 'uvis_flt_0'
    __table_args__ = {'autoload':True}
#    uvisflt0_id = Column('id', Integer)
#    uvisflt0_id = relationship(Master, 
#        primaryjoin = ('uvisflt0_id' == Master.id),
#        backref='id')
