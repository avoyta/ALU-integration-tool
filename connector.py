import tools.logger as logger
import paramiko
import time


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
            shell.recv(1024)
            shell.send('environment no more\r\n')
            time.sleep(0.5)
            shell.recv(1024)
        except:
            print('Connection failed')
        try:
            output = {}
            for cmd in cmd_list:
                shell.send(cmd + '\r\n')
                time.sleep(1)
                output.update({cmd: '\n'.join(shell.recv(50000).decode('utf-8').split('\r\n')[1:])})
            shell.close()
            client.close()
            return output
        except UnboundLocalError:
            print("Could'n create SHELL on node {0}".format(host))

