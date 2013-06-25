#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
import server
import sys
import Command

class ServerConsoleThread(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock

	def run(self):
		while True:
			self.command = raw_input("command: ")
			if self.command == "list":
				self.PrintList()
				continue
			elif self.command == "kill":
				self.KillUser()
				continue
			elif self.command == "exit":
				self.CloseServer()
				break
			else:
				print "Command not found"

	def PrintList(self):
		if self.IsListEmpty(server.ClientsLogins):
			print "User's list is empty"
		else:
			print "***User list***"
			print server.ClientsLogins

	def KillUser(self):
		if self.IsListEmpty(server.ClientsLogins):
			print "User list is empty. You can't delete anyone"
		else:
			print "Write user name, to stop his work, or write @back to input other operation"
			self.login = raw_input("user login to kill: ")
			if self.login != "@back":
				if self.login in server.ClientsLogins:
					self.index = server.ClientsLogins.index(self.login)
					self.messageOut = Command.clientDisconnect
					server.ConnClient[self.index].GetSocket().send(self.messageOut)
					server.ConnClient[self.index].Close()
					del server.ClientsLogins[self.index]
				else:
					print "Can't find this login in list"
			else:
				return

	def IsListEmpty(self, listToCheck):
		if not listToCheck:
			return True
		else:
			return False

	def CloseServer(self):
		if self.IsListEmpty(server.ConnClient):
			print "Exit in Server Console"
			self.sock.close()
			sys.exit(0)
		else:
			for conn in server.ConnClient:
				conn.Close()
			self.sock.close()
