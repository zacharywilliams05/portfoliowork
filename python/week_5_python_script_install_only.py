#!/usr/bin/env python3
# By Zachary Williams
# using python to install apache on Web1
# 5/6/2021
#code works

#import
from pexpect import pxssh

#login
session = pxssh.pxssh()
session.login('192.168.0.111','justincase', 'Password01')
print('SSH Login Successful!')

#codes to install
session.prompt()
session.sendline('sudo apt update')
print('Doing the update')
session.prompt()
session.sendline('Password01')
print('Sent password')
session.prompt()
session.sendline('sudo apt install apache2')
print('Installing')
session.prompt()
session.sendline('y')
print('Sent yes line')
#enable auto-start apache
session.prompt()
session.sendline('sudo systemctl enable apache2')

print('Everything finished successfully!')
#exit
