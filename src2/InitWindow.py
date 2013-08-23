# -*- coding: utf-8 -*-   
import wx
import sys
import threading
from APLocation import *
from wigle_api_lite import *
from  threading import *
from GMaps import *
import time
#from scapyprobes import *

class InitWindow(wx.Frame):
	""" derive a new frame. """
	def __init__(self, parent, title):			
		
		wx.Frame.__init__(self, parent, title="Geolocalización de redes", size=(900,500))
				
		addAPButton = wx.Button(self, id=wx.ID_ANY, label="Agregar entrada")
		addAPButton.Bind(wx.EVT_BUTTON, self.addAP)
		
		deleteAPButton = wx.Button(self, id=wx.ID_ANY, label="Borrar entrada")
		deleteAPButton.Bind(wx.EVT_BUTTON, self.deletePositive)

		SearchButton = wx.Button(self, id=wx.ID_ANY, label="Identificar en Maps")
		SearchButton.Bind(wx.EVT_BUTTON, self.showGoogleMaps)

		self.apList = wx.ListView(id=wx.ID_ANY,name='apList', parent=self, style=wx.LC_REPORT)

		self.apList.InsertColumn(0, 'Nombre de Red', width=300)
		self.apList.InsertColumn(1, 'BSSID', width=300)
		self.apList.SetBackgroundColour(wx.Colour(255, 255, 255))

		self.positiveList = wx.ListBox(choices=[], id=wx.ID_ANY,name='positiveList', parent=self, style=0)		
		self.positiveList.SetBackgroundColour(wx.Colour(255, 255, 255))
		
		box1 = wx.BoxSizer(wx.VERTICAL)
		box1.Add(addAPButton)
		box1.AddSpacer(50)
		box1.Add(deleteAPButton)
		box1.AddSpacer(50)
		box1.Add(SearchButton)

		box = wx.BoxSizer(wx.HORIZONTAL)
		box.AddSpacer(10)
		box.Add(self.apList, 2, wx.ALL|wx.EXPAND,border =5)
		box.Add(box1, 0, wx.ALL|wx.EXPAND,border =5)			
		box.AddSpacer(10)
		box.Add(self.positiveList, 1, wx.ALL|wx.EXPAND,border =5)
		box.AddSpacer(10)

		self.SetAutoLayout(True)
		self.SetSizer(box)

		self.Layout()

		self.timer = wx.Timer(self)
		self.timer.Start(3000)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

		self.positives = {}

	def OnTimer(self, evt):
			self.loadFile()

	def uploadNewAPs(self):
		while(1):
			self.loadFile()
			time.sleep(2)


	def loadFile(self):
		fileap = open('../data/ap', 'r') 

		for line in fileap:
			data = line.split('|') #####   ( | ESCAPE CHARACTER FOR FILE (NOT WORKING FOR ANY WIFI WITH NAME WITH  | )
			if self.apList.FindItem(-1,data[0]) == -1:
				index = self.apList.InsertStringItem(sys.maxint,data[0])
				self.apList.SetStringItem(index, 1, data[1])
		fileap.close()

	def getSelectedAP(self):
		index = self.apList.GetFirstSelected()

		if index !=  wx.NOT_FOUND:
			aps = []
			for col in range(self.apList.GetColumnCount()):
				aps.append((self.apList.GetItem(index, col).GetText()).encode("ascii")) 
			return aps
		else:
			return None

	def show(self):
		self.Show(True)
			
	def addAP(self,anEvent):
			
		anAP = self.getSelectedAP()
		if anAP is not None and self.positiveList.FindString(anAP[0])	== -1:
			self.positiveList.Append(anAP[0])
			self.positives[anAP[0]] = anAP[1]

	
	def deletePositive(self,anEvent):
		index = self.positiveList.GetSelection()
		if index !=  -1:
			self.positiveList.Delete(index)

	def showGoogleMaps(self,anEvent):				#no cierro la de busqueda sino que abro otra de resultados 
			
		sel = self.positiveList.GetSelection()
	
		#crear nueva ventana con positives
#		self.aMapsWindow = search_bssid(self.positives[self.positiveList.GetString(sel)])		

#		search_bssid(self.positiveList.GetString(sel))		
		
		print self.positiveList.GetString(sel)

		results = search_ssid(self.positiveList.GetString(sel))
	
		self.aMapsWindow =  MapsWindow(results)

		self.aMapsWindow.show()


