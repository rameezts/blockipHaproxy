#!/usr/bin/python
import re
import sys
import ipaddress
import os


# To block IP's - HaProxy
# Example: hablockip <IP Address>
i = 0
j = 0
file_path = r"/etc/haproxy/blacklist.lst"
get_ip = sys.argv[1]

try:
    ip = ipaddress.ip_address(get_ip)
    i = 1
except ValueError:
    print "*********************\nEnter a Valid IP\n********************"

if (i == 1):
    fl = open(file_path, 'r')
    lines = fl.read().split('\n')
    for line in lines:
        if line == get_ip:
            j = 1
    fl.close()
    if (j == 0):
        f = open(file_path, 'a')
        if os.path.getsize(file_path) > 0:
            f.write("\n" + get_ip)
            print "****************************\nBlocked new IP: %s\n****************************" % (get_ip)
            os.system("/etc/init.d/haproxyctl reload")
        else:
            f.write(get_ip)
            print "****************************\nBlocked new IP: %s\n****************************" % (get_ip)
            os.system("/etc/init.d/haproxyctl reload")
        f.close()
    else:
        print "********************\nDuplicate Entry\n********************"
