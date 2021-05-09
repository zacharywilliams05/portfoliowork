#!/usr/bin/env python3
# By Zachary Williams
# using python to install apache on Web1
# 5/6/2021
#code works

#import
from pexpect import pxssh
db_ip = ['192.168.0.121', '192.168.0.122']
web_ip = ['192.168.0.111', '192.168.0.112']

#create for loop web servers
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
    session.sendline('sudo apt install apache2')
    print('Installing')
    session.prompt()
    session.sendline('y')
    print('Sent yes line')
    #enable auto-start apache
    session.prompt()
    session.sendline('sudo systemctl enable apache2')

    print('Installation successful')

    #add user

        #add new user
    #add new user
    session.prompt()
    session.sendline('sudo adduser zackwilliams')
    print('Sent adduser command')
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

    #exit
    session.prompt()
    session.sendline('exit')
    print('Exited your session.')

#create loop for db servers
for i in db_ip:
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
    print('Installation successful!')

#add new user
    session.prompt()
    session.sendline('sudo adduser zackwilliams')
    print('Sent adduser command')
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

    #exit
    session.prompt()
    session.sendline('exit')
    print('Exited your session.')

