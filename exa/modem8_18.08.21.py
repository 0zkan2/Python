#!/usr/bin/env python3
# Import scapy

import scapy.all as scapy
# We need to create regular expressions to ensure that the input is correctly formatted.
import re

# Basic user interface header
print(r"""
||       || / |||||||||||| / ||||||||||
||       || / ||           / ||      ||
||       || / ||  |||||||| / ||      ||
||       || / ||        || / ||---|||
||       || / ||        || / ||     ||
||||||||||| / |||||||||||| / ||       ||

""")
print("\n****************************************************************")
print("\n*                              *")
print("\n*                                 *")
print("\n*                              *")
print("\n****************************************************************")


ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")


while True:
    ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to ("
                                 "ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break

arp_result = scapy.arping(ip_add_range_entered)
