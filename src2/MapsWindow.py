import sys
import re   
import wx
from maps import * 
from maps2 import *
from subprocess import call


class WifiInfo:
	def __init__(self, longs, lat, name):
		self.long = longs
		self.lat = lat
		self.wifiName = name

class MapsWindow:
	""" derive a new frame. """
	def __init__(self, parent, title,positive):			
		
		self.aps = positive

	def show(self):
		print "HOLA"

		# define a series of location markers and their styles
		# syntax:  markers=markerStyles|markerLocation1|markerLocation2|... etc.
		marker_list = []
		marker_list.append("markers=color:blue|label:S|11211|11206|11222") # blue S at several zip code's centers
		marker_list.append("markers=size:tiny|label:B|color:0xFFFF00|40.702147,-74.015794|") # tiny yellow B at lat/long
		marker_list.append("markers=size:mid|color:red|label:6|Brooklyn+Bridge,New+York,NY") # mid-sized red 6 at search location
		# see http://code.google.com/apis/maps/documentation/staticmaps/#Markers
		
		# make map that shows all the markers
		#get_static_google_map("google_map_example3", imgsize=(640,640), imgformat="png", markers=marker_list )

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
		open('map.htm','wb').write(g.showhtml())   # generate test file

		call(["firefox", "map.htm"])

