#!/usr/bin/python3
import tools.logger as logger
import paramiko
import time

# setup logging
paramiko.util.log_to_file('./logs/SSH.log')
LOG = logger.getLogger('Connector')

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def run_cmd(host, user, passwd, cmd_list, client=ssh_client, port_number=22):
    if type(cmd_list) is str:
        cmd_list = [cmd_list]
    try:
        client.connect(
            hostname=host,
            port=port_number,
            username=user,
            password=passwd,
            allow_agent=False)
        shell = client.invoke_shell()
        LOG.info('Successfully connected to {0}'.format(host))
        shell.recv(1024)
        shell.send('environment no more\r\n')
        time.sleep(0.5)
        shell.recv(1024)
    except:
        LOG.warning('Connection to {0} failed'.format(host))
    try:
        output = {}
        for cmd in cmd_list:
            shell.send(cmd + '\r\n')
            LOG.info('Executing command [ {0} ]'.format(cmd))
            time.sleep(1)
            output.update({cmd: '\n'.join(shell.recv(50000).decode('utf-8').split('\r\n')[1:])})
            LOG.info('Command [ {0} ] output received'.format(cmd))
        shell.close()
        client.close()
        LOG.info('Connection to {0} closed'.format(host))
        return output
    except:
        pass
