#! /usr/bin/env python

'''
This module reads in the .psf files.
'''

import glob
import numpy as np
import os 

from psf_database_interface import session
from psf_database_interface import PSFTable

def make_psf_dict(filename):
    '''
    '''
    with open(filename, 'r') as f:
        data = f.readlines()
        if len(data) != 0:
            line_counter = 0
            for line in data:
                line = line.strip().split()
                if line_counter == 0:
                    psf = {'psf':'', 'model_fraction':'', }
                    for item in psf:
                        psf[item] = np.zeros((121))
                    psf['filename'] = os.path.basename(filename)
                    psf['psf_x_center'] = int(line[0]) + 5
                    psf['psf_y_center'] = int(line[1]) + 5
                    psf['model_x_center'] = float(line[3]) + 5
                    psf['model_y_center'] = float(line[4]) + 5
                    psf['psf_flux'] = int(float(line[5]))
                    psf['sky']= float(line[6])
                if line_counter <= 120:
                    psf['psf'][line_counter] = line[2]
                    psf['model_fraction'][line_counter] = line[7]
                    line_counter += 1
                if line_counter == 120:
                    psf['psf'] = np.flipud(np.transpose(psf['psf'].reshape(11,11)))
                    psf['psf'] = str(psf['psf'].ravel())
                    psf['model_fraction'] = np.flipud(np.transpose(psf['model_fraction'].reshape(11,11)))
                    psf['model_fraction'] = str(psf['model_fraction'].ravel())
                    line_counter = 0
                    psf_table = PSFTable(psf)
                    session.add(psf_table)
        else:
            psf_table = None
    return psf_table


def plot_psf(psf):
    '''
    Plot the psf in the dictionary.
    '''
    import matplotlib.pyplot as plt 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    p = ax.imshow(psf['psf'].reshape(11,11), interpolation='nearest')
    plt.colorbar(p)
    plt.show()


def read_psf_files_main():
    '''
    Main controller for the read_psf_files module.
    '''
    count = 0
    for filename in glob.glob('/grp/hst/wfc3c/viana/psf/outputs/*.psf'):
        count += 1
        print 'Working on number {}'.format(count)
        psf_table = make_psf_dict(filename)
        if psf_table != None:
            session.commit()


if __name__ == '__main__':
    read_psf_files_main()