__author__ = 'avoyta'
#!/usr/bin/python3
#coding=utf-8

import ftplib

def get_cfgfile_from_host(host, user, passwd, full_path, filename):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=passwd)
        ftp.cwd(full_path)
    except:
        print('Connection to FTP server {0} failed...'.format(host))
    try:
        if filename in ftp.nlst():
            print('File found... Trying to get it...')
            ftp.retrbinary('RETR {0}'.format(filename),
                           open('./CFGs/{0}_{1}.cfg'.format(filename[:-4],
                                                            host.replace('.', '-')), 'wb').write)
            print('Download successful...')
        else:
            print('File {0} not found in {1}:{2}'.format(filename, host, full_path))
        ftp.close()
    except:
        pass

def list_ftpdir(host, user, passwd, full_path):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=passwd)
        ftp.cwd(full_path)
    except:
        print('Connection to FTP server {0} failed...'.format(host))
    try:
        for file in ftp.nlst():
            print(file)
    except:
        pass