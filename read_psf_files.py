#! /usr/bin/env python

'''
This module reads in the .psf files.
'''

import glob
import numpy as np 

from psf_database_interface import session
from psf_database_interface import PSFTable

def make_psf_dict(filename):
    '''
    '''
    with open(filename, 'r') as f:
        data = f.readlines()
        if len(data) != 0:
            line_counter = 0
            psf = {'psf':'', 'sky':'', }
            for item in psf:
                psf[item] = np.zeros((121))
            for line in data:
                line = line.strip().split()
                if line_counter == 0:
                    psf['x_center'] = int(line[0]) + 5
                    psf['y_center'] = int(line[1]) + 5
                if line_counter <= 120:
                    psf['psf'][line_counter] = line[2]
                    line_counter += 1
                if line_counter == 120:
                    psf['psf'] = np.flipud(np.transpose(psf['psf'].reshape(11,11)))
                    psf['psf'] = psf['psf'].ravel()
                    line_counter = 0
                    psf_table = PSFTable(
                        psf['x_center'], 
                        psf['y_center'], 
                        str(psf['psf']))
                    session.add(psf_table)
        else:
            psf = None
    return psf


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
    for filename in glob.glob('../data/*.psf'):
        psf = make_psf_dict(filename)
        if psf != None:
            write_to_database(psf)
            session.commit()

if __name__ == '__main__':
    read_psf_files_main()