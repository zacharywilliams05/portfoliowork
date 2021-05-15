#!/usr/bin/env python3
# By Zachary Williams
# using python to install apache on Web1
# 5/6/2021
#code works

#import
from pexpect import pxssh
all_ip = ['192.168.0.112', '192.168.0.122']

#create for loop
for i in all_ip:
    #login
    session = pxssh.pxssh()
    session.login(i,'justincase', 'Password01')
    print('SSH Login Successful to {0}'.format(i))
    
    #add new user
    session.prompt()
    session.sendline('sudo adduser zackwilliams')
    session.prompt()
    session.sendline('Password01')
    print('Sent password')
    session.prompt()
    session.sendline('dackarypilliams')
    session.prompt()
    session.sendline('dackarypilliams')
    print('Password set')
    session.prompt()
    session.sendline('Zack Williams')
    print('Added name')
    session.prompt()
    session.sendline('42')
    print('Added room')
    session.prompt()
    session.sendline('2533333333')
    print('Added work #')
    session.prompt()
    session.sendline('3603333333')
    print('Added home #')
    session.prompt()
    session.sendline('Worker')
    print('Added group')
    session.prompt()
    session.sendline('y')
    print('User added')