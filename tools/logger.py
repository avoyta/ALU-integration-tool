__author__ = 'agorbachev'
import logging
from os import path,curdir

def getLogger(__name):
    '''
    :param __name: logger name. Is used to create file at log folder.
    :return: logger object with 2 handlers. First handler logging to file and second handler print to console
    '''
    #TODO:agorbachev:develop log formatter
    formatter = logging.Formatter('%(name)s: %(levelname)s \t%(asctime)s: %(message)s')

    LOG = logging.getLogger(__name)
    #TODO:agorbachev:add logging level selection
    LOG.setLevel(logging.DEBUG)
    #add Handler writing log to file
    #TODO:agorbachev:develop user timestamp for logging actions
    LOGFileHandler = logging.FileHandler(path.join(curdir, 'logs', '{0}.log'.format(__name)))
    LOGFileHandler.setLevel(logging.DEBUG)
    LOGFileHandler.setFormatter(formatter)
    LOG.addHandler(LOGFileHandler)
    #add Handler writing log to console
    LOGStreamHandler = logging.StreamHandler()
    LOGStreamHandler.setLevel(logging.DEBUG)
    LOGStreamHandler.setFormatter(formatter)
    LOG.addHandler(LOGStreamHandler)

    return LOG
