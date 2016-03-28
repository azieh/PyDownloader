#Nmap Port Scanner

import nmap
import threading
import time

def nmap_scan(tgtHost, tgtPort):
    try:
	    nscan = nmap.PortScanner()
	    nscan.scan(tgtHost, tgtPort)
	    state = nscan[tgtHost]['tcp'][int(tgtPort)]['state']
	    print(" [*] " + tgtHost + " tcp/" +tgtPort + " " + state)
    except Exception as e:
        pass

if __name__ == '__main__':
    instance = []
    for x in range(1,255):
        ip = "83.7.2." + str(x)
        try:

            instance.append(threading.Thread(target=nmap_scan, args=(ip, "80")))
            instance[x-1].start()
            time.sleep(0.001)
            print(ip)
        except Exception as e:
            print(e)
            raise
