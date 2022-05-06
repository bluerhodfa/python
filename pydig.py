#!/usr/bin/env python3

import re
import socket
import dns.resolver
from sys import argv

def main():
    domains = argv[1:]

    for domain in domains:
        print(f'-- DOMAIN: {domain}')
        ip = dns.resolver.resolve(domain, 'A')
        print(f'IP: {ip[0].to_text()}')

        for rdata in dns.resolver.resolve(domain, 'NS'):
            print(f'NS: {rdata.target.to_text()}')

        fqn = domain if re.search('^www.', domain) else f'www.{domain}'
        for rdata in dns.resolver.resolve(fqn, 'CNAME'):
            print(f'CNAME: {rdata.target}')

if __name__ == '__main__':
    main()

