# -*- coding: utf-8 -*-   
import wx
import sys
import re   
from maps import * 
from maps2 import *
import wx.html

class WifiInfo:
	def __init__(self, longs, lat, name):
		self.long = longs
		self.lat = lat
		self.wifiName = name

class MyHtmlFrame(wx.Frame):

	def showMap(self):
			g = PyMap()                         # creates an icon & map by default
			icon2 = Icon('icon')               # create an additional icon
			icon2.image = "http://labs.google.com/ridefinder/images/mm_20_blue.png" # for testing only!
			icon2.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png" # do not hotlink from your web page!
			g.addicon(icon2)
			g.key = "ABQIAAAAQQRAsOk3uqvy3Hwwo4CclBTrVPfEE8Ms0qPwyRfPn-DOTlpaLBTvTHRCdf2V6KbzW7PZFYLT8wFD0A" # you will get your own key
			g.maps[0].zoom = 11
	#		q = [1,1]                           # create a marker with the defaults
	#		r = [2,2,'','icon2']                # icon2.id, specify the icon but no text
	#		s = [3,3,'hello, <u>world</u>']     # don't specify an icon & get the default
			self.aps = [WifiInfo(-34,-58,'WIFI 1'),WifiInfo(-33,-58,'WIFI 2'),WifiInfo(-34,-57,'WIFI 3')]		

			for pos in self.aps:
				print "HELLO"
				point = [pos.long, pos.lat, pos.wifiName]		
				g.maps[0].setpoint(point)               # add the points to the map

		##    print g.showhtml()
			open('test.htm','wb').write(g.showhtml())   # generate test file
	
			return g

	def __init__(self, parent, title,positive):

		self.aps = positive

		wx.Frame.__init__(self, parent, -1, title)

		html = wx.html.HtmlWindow(self)

		if 'gtk2' in wx.PlatformInfo:

				html.SetStandardFonts()

		html.SetPage(self.showMap().showhtml())

