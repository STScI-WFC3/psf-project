#! /usr/bin/env python

'''
This module reads in the .psf files.
'''

import glob
import numpy as np 

def make_psf_dict():
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
                if line_counter <= 120:
                    line = line.strip().split()
                    psf['psf'][line_counter] = line[2]
                    line_counter += 1
                if line_counter == 120:
                    psf['psf'] = np.flipud(np.transpose(psf['psf'].reshape(11,11)))
                    psf['psf'] = psf['psf'].ravel()
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

if __name__ == '__main__':
    read_psf_files_main()