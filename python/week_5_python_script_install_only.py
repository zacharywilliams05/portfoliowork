#!/usr/bin/env python3
# By Zachary Williams
# using python to install apache on Web1
# 5/6/2021

#import
from pexpect import pxssh

#login
session = pxssh.pxssh()
session.login('192.168.0.111','justincase', 'Password01')
print('SSH Login Successful!')

#codes to install


#exit