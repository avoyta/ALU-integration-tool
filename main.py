__author__ = 'agorbachev'
import tools.logger as logger
import time
import connector
#TODO:add logging level as script parameter

# LOG = logger.getLogger('IntegrationTool')
# UserLOG = logger.getLogger('UserLOG')
# while True:
#     LOG.debug('Main logging test')
#     UserLOG.info('User log')
#     time.sleep(1)

try:
    for cmd, output in connector.run_cmd('172.17.14.95', 'admin', 'admin', '/admin save').items():
        print('#', cmd)
        print(output)
except AttributeError:
    print("Can't run command on remote node")

