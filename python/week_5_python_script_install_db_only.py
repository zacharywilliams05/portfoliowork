#!/usr/bin/env python3
# By Zachary Williams
# using python to install apache on Web1
# 5/6/2021
#code works

#import
from pexpect import pxssh
db_ip = ['192.168.0.121', '192.168.0.122']

#create for loop
for i in web_ip:
    #login
    session = pxssh.pxssh()
    session.login(i,'justincase', 'Password01')
    print('SSH Login Successful to {0}'.format(i))

    #codes to install
    session.prompt()
    session.sendline('sudo apt update')
    print('Doing the update')
    session.prompt()
    session.sendline('Password01')
    print('Sent password')
    session.prompt()
    session.sendline('sudo apt install mariadb-server')
    print('Installing')
    session.prompt()
    session.sendline('y')
    print('Sent yes line')
    #enable auto-start apache
    session.prompt()
    session.sendline('sudo systemctl enable mariadb.service')

    print('Everything finished successfully!')
    #exit