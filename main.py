__author__ = 'agorbachev'
import tools.logger as logger
import time
#TODO:add logging level as script parameter

LOG = logger.getLogger('IntegrationTool')
UserLOG = logger.getLogger('UserLOG')
while True:
    LOG.debug('Main logging test')
    UserLOG.info('User log')
    time.sleep(1)

