#!/usr/bin/python3
__author__ = 'agorbachev'
import tools.logger as logger
import time
import connector
from threading import Event
#TODO:add logging level as script parameter

# LOG = logger.getLogger('IntegrationTool')
# UserLOG = logger.getLogger('UserLOG')
# while True:
#     LOG.debug('Main logging test')
#     UserLOG.info('User log')
#     time.sleep(1)

commands_list = [
    '/configure system security ftp-server',
    '/configure system security user admin access ftp',
    '/admin save'
]
host_list = [
    '172.17.14.63',
    '172.17.14.81',
    '172.17.14.82',
    '172.17.14.72',
    '172.17.14.73',
    '172.17.14.94',
    '172.17.14.95',
]
# host_list = ['172.17.14.73']

tmp = {}
for host in host_list:
    try:
        tmp = connector.run_cmd(host, 'admin', 'admin4', commands_list)
        # time.sleep(10)
    except AttributeError:
        print("Can't run command on remote node")

    if tmp:
        for cmd in commands_list:
            print('#', cmd)
            print(tmp[cmd])

