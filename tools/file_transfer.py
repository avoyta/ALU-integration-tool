__author__ = 'avoyta'
#!/usr/bin/python3
#coding=utf-8

import ftplib
import os

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

def put_cfgfile_to_host(host, user, passwd, local_full_path, filename, dst_full_path):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=passwd)
        ftp.cwd(dst_full_path)
    except:
        print('Connection to FTP server {0} failed...'.format(host))
    os.chdir(local_full_path)
    if os.path.exists(filename):
        try:
            ftp.storbinary('STOR {0}'.format(filename), open(filename, 'rb'))
            if filename in ftp.nlst():
                print('{0} upload successfully...'.format(filename))
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