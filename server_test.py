#!/usr/bin/env python
#-*- coding:cp1251 -*-
import server
import unittest

class Test(unittest.TestCase):
	def setUp(self):
		self.seq = range(1024,5000)
		port = 5001
		self.test_server = server.Server(port)

	def test_FindFreePort(self):
		self.test_server.FindFreePort()
		self.assertTrue(self.test_server.port in self.seq)

	def test_Close(self):
		self.test_server.Close()
		self.assertIs(len(server.ConnClient), 0)	
if __name__=="__main__":
	unittest.main()
		