#! /usr/bin/env python

import multiprocessing
import os
import socket
import subprocess

from ql_database_interface import Master
from ql_database_interface import UVISFLT0
from ql_database_interface import session
from ql_database_interface import SETTINGS

from sqlalchemy import cast
from sqlalchemy import REAL

FILTER_LIST = ['F225W', 'F275W', 'F336W', 'F390W', 'F438W', 'F555W', \
    'F606W', 'F775W', 'F814W', 'F850L']

if __name__ == '__main__':
    query = session.query(UVISFLT0, Master)\
        .join(Master, Master.id == UVISFLT0.id)\
        .filter(cast(UVISFLT0.EXPTIME, REAL) >= 400.0)\
        .filter(UVISFLT0.TARGNAME != 'DARK').all()        
    
    job_list = []    

    for record in query:
        fits_file =  os.path.join(record.Master.dir, record.Master.filename)
        if record.UVISFLT0.FILTER in FILTER_LIST:
            job_list.append(['/grp/hst/wfc3c/viana/psf/jays-code/img2psf_wfc3uv.e', 
                '7', '10000', '59000', 
                '/grp/hst/wfc3c/viana/psf/psf-models/PSFEFF_WFC3UV_{}_C0.fits'.format(record.UVISFLT0.FILTER), 
                'QSEL', fits_file])
            print job_list
            import sys
            sys.exit()


    pool = multiprocessing.Pool(processes=SETTINGS[socket.gethostname()]['cores'])
    pool.map(subprocess.call, job_list)
    pool.close()

