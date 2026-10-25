"""
01. Network Intrusion Detection System (IDS)
Purpose: Detect potential TCP SYN port scans using Scapy.

REQUIRED PACKAGES:
  * pip install scapy
  * Tested on: pip 26.1.2 | scapy==2.8.0
"""
from collections import defaultdict
import time

try:
    # pyrefly: ignore[missing-import]
    from scapy.all import sniff, IP, TCP

    ports, start = defaultdict(set), {}

    def detect(p):
        if IP not in p or TCP not in p:
            return
        # Flag 2 = SYN, Flag 16 = ACK (SYN scan: SYN set without ACK)
        if p[TCP].flags & 2 and not (p[TCP].flags & 16):
            ip, now = p[IP].src, time.time()
            if ip not in start or now - start[ip] > 10:
                ports[ip], start[ip] = set(), now
            ports[ip].add(p[TCP].dport)
            if len(ports[ip]) >= 10:
                print(f"[ALERT] Possible port scan from {ip} on {len(ports[ip])} ports")

    # Demonstration test with synthetic SYN scan packets:
    print("[*] Testing detector with simulated SYN scan traffic...")
    for target_port in [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]:
        detect(IP(src="192.168.1.45")/TCP(dport=target_port, flags="S"))

    # Live sniff (uncomment to monitor live network traffic):
    # print("[*] Monitoring TCP packets for SYN port scans...")
    # sniff(filter="tcp", prn=detect, store=False)

except ImportError:
    print("[!] Scapy not installed. Run: pip install scapy")

"""
SAMPLE OUTPUT:
[*] Testing detector with simulated SYN scan traffic...
[ALERT] Possible port scan from 192.168.1.45 on 10 ports
"""
