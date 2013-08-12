#!/usr/bin/env python
# getAPLocation v4 by Geordie
# you no longer need to specify the cookie here. just run as normal, and it will ask you to login.
import re
import webbrowser
import httplib, urllib, sys, string, getpass


def doLogin(username,password):
	params = urllib.urlencode({'credential_0': username, 'credential_1': password, 'noexpire':'on'})
	headers = {"Accept-Encoding":"text/plain"}
	conn = httplib.HTTPConnection("wigle.net")
	conn.request("POST", "/gps/gps/main/login/", params, headers)
	reply = conn.getresponse()
	if (reply.status == 302):
		print "Successful login - do this again in 10 years"
		data = reply.getheader("Set-Cookie").split(";")
		return data[0]
	if (reply.status == 200):
		print "Login failed - check username/password"
		return ""

def save_cookie(cookie):
	try:
		f = open('wigle_cookie', 'w')
		f.write(cookie)
		f.close()
	except:
		print "Error saving cookie! Check that wigle_cookie can be created and/or written to."

def load_cookie():
	cookie = "auth=zerokes%3A758447942%3A1375992219%3A6PRWiIpohn7Vxk7UQvIrZA"
	return cookie

def search_bssid(netid):
	
	cookie = load_cookie()
	ssid = 1
	bssid = 0
	if ":" in netid:
		numberOfOctets = netid.count(":")
		if (numberOfOctets != 5):
			print "Invalid BSSID - %i octets found (should have 6)" %  (numberOfOctets + 1)
			sys.exit()
		length = len(netid)
		if (length != 17):
			print "Invalid BSSID - %i characters long (should be 17)" % length
	
	try:
		headers = {"Accept-Encoding":"text/plain", "Cookie":cookie}
		conn = httplib.HTTPSConnection("wigle.net")
		if (ssid == 1):
			conn.request("GET", ("/gps/gps/main/confirmquery/?ssid=%s&simple=true" % netid), "", headers)
		if (bssid == 1):
			#http://wigle.net/gps/gps/main/confirmquery/?netid=E0:69:95:67:95:92&amp;simple=true
			conn.request("GET", ("/gps/gps/main/confirmquery/?netid=%s&simple=true" % netid), "", headers)

		reply = conn.getresponse()
		data = reply.read()
		print data
	except:
		print "Error connecting to WiGLE!"

	try:
		string = '/gps/gps/Map/onlinemap2/.*">Get Map</a>'
		extractor = re.compile(r'%s' %string)
		results = re.findall(extractor,data)
		#supongo que devuelve un uno link 

		for res in results: 
			link = res.split('"')[0]
			webbrowser.open("http://wigle.net"+link)

		conn.close()

	except:
		print "Error searching."
