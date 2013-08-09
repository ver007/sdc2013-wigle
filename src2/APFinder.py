# -*- coding: utf-8 -*-   
import socket
import sys
import SocketServer
from wx import *
from InitWindow import InitWindow
from linecache import getline	

class APFinder(App):
	def __init__(self):
		wx.App.__init__(self)

		self.aInitWindow = InitWindow(None, 'AP Finder')	
	
		self.aInitWindow.show()

		
client = APFinder()
client.MainLoop()
