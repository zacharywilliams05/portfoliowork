#!/usr/bin/env python3
# By Zachary Williams
# using python to add a user, install programs on a remote machine
# 5/6/2021

import pexpect

child = pexpect.spawn('ssh justincase@192.168.0.121')
child.expect('.*password:')
child.sendline('Password01')

print('SSH login successful')
