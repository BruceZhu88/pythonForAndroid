# -*- coding: utf-8 -*-
import ftplib
import time
import os, sys, time
def now():
	return time.strftime('%Y-%m-%d %X',time.localtime())

if len( sys.argv ) ==2:
    filename = sys.argv[1]
else:
    print 'usage: upload.py file1 '
    sys.exit(1)

if not os.path.exists(filename):
    print 'ERROR: %s not found\n' % filename
    sys.exit(1)

# upload a file to a ftp server.
HOST = '10.10.10.147'
PORT = '2121'
USER = 'qpy3'
PASS = 'qpy3'
REMOTE = 'scripts'
LOCAL = '/storage/sdcard1/com.hipipal.qpyplus/'
#print LOCAL
os.chdir(filename)

ftp = ftplib.FTP()
ftp.connect(HOST,PORT)
ftp.login(USER,PASS)
ftp.cwd(REMOTE)

bufsize = 1024
file_handler = open(LOCAL +filename,'rb')
# 上传文件
ftp.storbinary('STOR '+filename, file_handler,bufsize) 
# 关闭文件
file_handler.close() 
ftp.quit()
print 'upload', filename, 'at', now( )