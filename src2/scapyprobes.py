from scapy.all import *

observedClients = []

def PacketHandler(pkt):
	
	if pkt.haslayer(Dot11) :
		if pkt.type == 0 and pkt.subtype == 4 :
			print "Client with MAC: %s probing for SSID %s con BSSID" %(pkt.addr2, pkt.info,pkt.addr1)
			if pkt.addr1 not in observedClients:
					fileap = open('../data/ap', 'a') 
					fileap.write('%s %s\n'%(pkt.addr1, pkt.info))
					print "Escribiendo en archivo %s %s\n" %(pkt.addr1, pkt.info)
					observedClients.append(pkt.addr1)
					fileap.close()

sniff(iface="mon0", prn = PacketHandler)
