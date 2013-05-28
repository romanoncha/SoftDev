#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Server import *
from Client_Threading import ClientThreading

# GLOBAL
default_port = 3030

server = Server(default_port)
server.Start()
server.Close()