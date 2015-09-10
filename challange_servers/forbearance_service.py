#!/usr/bin/python2

import os
import socket
import sys
from thread import start_new_thread

from binascii import hexlify

PATH = os.path.dirname(__file__)
KEYFILE = PATH+'/'+'forbearance_keyfile'
HOST = ''
PORT = 1214


def import_key():	

	keyfile = open(KEYFILE, 'rb')
	key = keyfile.read(64)
	keyfile.close()

	print '[*] Key: %s' % hexlify(key[:32]) 
	print '[*] IV:  %s' % hexlify(key[32:])
	return key


def initialize():

	server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server_sock.bind((HOST,PORT))
	except socket.error, message:
		print('Bind failed. Error: {}'.format(message[1]))
		sys.exit()

	server_sock.listen(10)
	print '[*] Listening on [%s:%d]' % (HOST, PORT)
	return server_sock


def client_thread(conn,addr):

    try:
	data = conn.recv(1024)
	data = data.strip()
	print '[*] Data from %s: [%s]' % (addr,data)
	if data == 'Computer Maintenance Competition Assurance Act':
		print '[*] Sending key data to %s (%d bytes)' % (addr, len(key))
		client_conn.sendall(key)
	conn.close()
    except:
        pass


key = import_key()
server_sock = initialize()

while 1:
	client_conn, client_addr = server_sock.accept()
	print '[*] Received connection from [%s:%d]' % (client_addr[0], client_addr[1])
	start_new_thread(client_thread, (client_conn,client_addr[0]))

print '[*] Shutting down'
client_conn.close()
server_sock.close()
