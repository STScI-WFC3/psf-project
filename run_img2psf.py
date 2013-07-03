#! /usr/bin/env python

import os
import subprocess

from dborm import Master
from dborm import UVISFLT0
from dborm import session

from sqlalchemy import cast
from sqlalchemy import Real

if __name__ == '__main__':
    query = session.query(UVISFLT0, Master)\
        .join(Master, Master.id == UVISFLT0.id)\
        .filter(UVISFLT0.FILTER == 'F606W')\
        .filter(cast(UVISFLT0.EXPTIME, Real) >= 400.0)\
        .filter(UVISFLT0.TARGNAME != 'DARK').all()        
    
    for record in query:
        fits_file =  os.path.join(record.Master.dir, record.Master.filename)
        subprocess.call(['../img2psf_wfc3uv.e', '7', '10000', '59000', 
            '../PSFEFF_WFC3UV_F606W_C0.fits', 'QSEL', fits_file])