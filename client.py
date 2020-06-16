#!/usr/bin/python
import socket, select, string, sys

def prompt():
	sys.stdout.write('<anda> ')
	sys.stdout.flush()

if __name__ == "__main__":
	if(len(sys.argv) < 3):
		print 'gunakan syntax yang benar : python chat_client.py hostname port'
		sys.exit()
	host = sys.argv[1]
	port = int(sys.argv[2])
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	
	try:
		s.connect((host, port))
	except:
		print 'Tidak Bisa Konek'
		sys.exit()
	
	print 'Berhasil konek ke remote host. mulai kirim pesan!'
	prompt()
	
	while 1:
		socket_list = [sys.stdin, s]
		
		read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
		
		for sock in read_sockets:
			if sock == s:
				data = sock.recv(4096)
				if not data:
					print '\nTerputus dari chat server'
					sys.exit()
				else:
					sys.stdout.write(data)
			
			else:
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()

			