import socket
import time
from collections import defaultdict

class ClientError(Exception):
   pass

class Client:

	def __init__(self, host, port, timeout = None):
		self.host = host
		self.port = port
		self.timeout = timeout
		# try:
		# 	self.connection = socket.create_connection((host, port), timeout)
		# except socket.error as ex:
		# 	raise ClientError("client error", ex)

	def put(self, key, value, timestamp = None):
		self.key = key
		self.value = value
		self.timestamp = timestamp or int(time.time())
		with socket.create_connection((self.host, self.port), self.timeout) as sock:
			try:			
				sock.sendall(f"put {key} {value} {timestamp}\n".encode("utf8"))
				data = sock.recv(1024).decode()
				if data == 'error\nwrong command\n\n':
					raise ClientError
			except socket.error:
				raise ClientError

	def get(self, key):
		d = defaultdict(list)
		self.key = key or "*" or 'key_not_exists'
		if self.key == key:
			with socket.create_connection((self.host, self.port), self.timeout) as sock:
				try:				
					sock.sendall(f"get {key}\n".encode("utf8"))
				except socket.error as ex:
					raise ClientError("client error", ex)

				data = sock.recv(1024).decode("utf8")

				data = [i.split() for i in data.split('\n')[1:] if len(i) > 1]
				# print(len(data))

				for i in data:
					try:
						d[i[0]].append((int(i[2]), float(i[1])))
					except IndexError as ex:
						raise ClientError("get_client_error", ex)


		if self.key == '*':
			return d
		elif self.key == 'key_not_exists':
			return {}
		else:
			return d