# -*- coding: utf-8 -*-  
import ftplib  
import os  
import socket  
  
HOST = 'ftp://192.168.1.104:2121'  
DIRN = '/storage/emulated/0/com.hipipal.qpyplus'  
FILE = 'Speech_recog_Bing.py'  
def main():  
    try:  
        f = ftplib.FTP(HOST)  
    except (socket.error, socket.gaierror):  
        print 'ERROR:cannot reach " %s"' % HOST  
        return  
    print '***Connected to host "%s"' % HOST  
  
    try:  
        f.login()  
    except ftplib.error_perm:  
        print 'ERROR: cannot login anonymously'  
        f.quit()  
        return  
    print '*** Logged in as "anonymously"'  
    try:  
        f.cwd(DIRN)  
    except ftplib.error_perm:  
        print 'ERRORL cannot CD to "%s"' % DIRN  
        f.quit()  
        return  
    print '*** Changed to "%s" folder' % DIRN  
    try:  
        #��һ���ص�������retrbinary() ����ÿ����һ������������ʱ���ᱻ����  
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)  
    except ftplib.error_perm:  
        print 'ERROR: cannot read file "%s"' % FILE  
        os.unlink(FILE)  
    else:  
        print '*** Downloaded "%s" to CWD' % FILE  
    f.quit()  
    return  
  
if __name__ == '__main__':  
    main()  