from scapy.all import *

observedClients = []

def PacketHandler(pkt):
	
	if pkt.haslayer(Dot11) :
		if pkt.type == 0 and pkt.subtype == 4 :
			print "Client with MAC: %s probing for SSID %s con BSSID %s" %(pkt.addr2, pkt.info,pkt.addr1)
			if pkt.info not in observedClients and pkt.info != "":
					fileap = open('../data/ap', 'a') 
					fileap.write('%s %s\n'%( pkt.info, pkt.addr1))
					print "Escribiendo en archivo %s %s\n" %(pkt.addr1, pkt.info)
					observedClients.append(pkt.info)
					fileap.close()

def startSniffing():	
	try:
		sniff(iface="mon0", prn = PacketHandler)
	except KeyboardInterrupt:
		join()
		pass

