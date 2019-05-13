#!/usr/bin/env python

from __future__ import print_function

import socket
import dns.resolver

# Basic query
for rdata in dns.resolver.query('www.bluerhodfa.com', 'CNAME'):
    print(rdata.target)

# Set the DNS Server
resolver = dns.resolver.Resolver()
resolver.nameservers = [socket.gethostbyname('ns1.alextheobold.com')]
for rdata in resolver.query('www.fatladtofitdad.com', 'CNAME'):
    print(rdata.target)
