'''
Read in the machine-specific yaml configuration file.
'''

import socket
import yaml

def get_settings():
    '''
    Gets the setting information that we don't want burned into the 
    repo.
    '''
    with open('/grp/hst/wfc3c/viana/psf/psf-project/config.yaml', 'r') as f:
        data = yaml.load(f)
    return data

SETTINGS = get_settings()[socket.gethostname()]
