#!/usr/bin/env python3
import argparse
import socket
from time import sleep


ANNOUNCEMENT_TEMPLATE = \
    "NOTIFY * HTTP/1.1\r\n" \
	"Host: 239.255.255.250:1990\r\n" \
	"Server: Buildroot/2018.02-rc3 UPnP/1.0 ssdpd/1.8\r\n" \
	"Location: {printerip}\r\n" \
	"NT: urn:bambulab-com:device:3dprinter:1\r\n" \
	"NTS: ssdp:alive\r\n" \
	"USN: 00M09C410701524\r\n" \
	"Cache-Control: max-age=1800\r\n" \
	"DevModel.bambu.com: BL-P001\r\n" \
	"DevName.bambu.com: {printername}\r\n" \
	"DevSignal.bambu.com: -58\r\n" \
	"DevConnect.bambu.com: lan\r\n" \
	"DevBind.bambu.com: free\r\n" \
	"Devseclink.bambu.com: secure\r\n" \
	"DevInf.bambu.com: wlan0\r\n" \
	"\r\n"

UDP_PORT_NO = 2021

def main(printerip, printername, interval=5.0):
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
    allips = [ip[-1][0] for ip in interfaces]

    msg = ANNOUNCEMENT_TEMPLATE.format(printerip='10.0.0.217', printername="UKS-UKS-UKS").encode()
    while True:

        for ip in allips:
            print(f'sending on {ip}')
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.bind((ip,0))
            sock.sendto(msg, ("255.255.255.255", UDP_PORT_NO))
            sock.close()

        sleep(interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "printerip",
        type=str,
        help="IPv4 address of the Bambu X1C printer (in LAN mode), e.g. 192.168.1.42")
    parser.add_argument(
        "printername",
        type=str,
        help="printer name as it appears in the device pane of OrcaSlicer/Bambustudio"
    )
    args = parser.parse_args()
    main(args.printerip, args.printername)
