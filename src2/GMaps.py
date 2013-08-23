# -*- coding: utf-8 -*-

import webbrowser
import sys
import re   
import wx
from maps2 import *
from subprocess import call


class WifiInfo:
  def __init__(self, longs, lat, name):
    self.long = longs
    self.lat = lat
    self.wifiName = name

class MapsWindow:
  """ derive a new frame. """
  def __init__(self,positive):      
		
		print positive
		print positive
		self.aps = positive

  def show(self):
    
	g = PyMap()                         # creates an icon & map by default
	icon2 = Icon('icon')               # create an additional icon
	icon2.image = "http://labs.google.com/ridefinder/images/mm_20_blue.png" # for testing only!
	icon2.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png" # do not hotlink from your web page!
	g.addicon(icon2)
	g.key = "ABQIAAAAQQRAsOk3uqvy3Hwwo4CclBTrVPfEE8Ms0qPwyRfPn-DOTlpaLBTvTHRCdf2V6KbzW7PZFYLT8wFD0A" # you will get your own key
	g.maps[0].zoom = 11

	for pos in self.aps:
		print  pos['lat']
		print pos['long']
	
		longitud = float(pos['long'])
		latitud = float(pos['lat'])
		point = [latitud,longitud, pos['ssid']]    
		g.maps[0].setpoint(point)               # add the points to the map

  ##    print g.showhtml()
	open('map.htm','wb').write(g.showhtml())   # generate test file

	webbrowser.open("map.htm")


