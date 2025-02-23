#!/usr/bin/env python3
import argparse
import socket
from time import sleep


SSDP_PORT_NO = 2021   # UDP port no. used for the discovery messages by the X1C


def main(bind_addr=''):
    print("Bambu X1C is sending SSDP discovery broadcast every few")
    print("seconds. If everything works you should see a message")
    print("real soon.")
    print('-------------------------------------------------------------')
    if bind_addr:
        print(f'Sniffing on address: {bind_addr}, hit Ctrl+C to stop')
    else:
        print(f'Sniffing, hit Ctrl+C to stop')
    print("=============================================================")
    while True:
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # sock.bind((bind_addr, SSDP_PORT_NO))
        sock.bind((bind_addr.encode(), SSDP_PORT_NO))
        message, address = sock.recvfrom(1024)
        lines = message.decode().split('\r\n')
        print(f"Message receive from {address}:")
        print('------------------------------->8----------------------------')
        print("BROADCAST_MESSAGE = ''.join([")
        for line in lines[:-1]:
            print(f"\t'{line}\\r\\n',")
        print("])")
        print('-------------------------------8<----------------------------')
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bind_addr",
        nargs="?",
        default='',
        type=str,
        help="IP address to bind the listening socket to.")
    args = parser.parse_args()
    try:
        main(args.bind_addr)
    except KeyboardInterrupt:
        print("Terminated by user.")
        exit(0)

