#!/usr/bin/env python3

import re
import socket
import dns.resolver
from sys import argv

class termColors:
    SUCCESS = '\033[92m'
    WARN = '\033[91m'
    DANGER = '\033[93m'
    ENDC = '\033[0m'

def validateArgs(args):
    if not len(args):
        print(f'{termColors.WARN}Required command line arguments not passed')
        print('Please use the following format...')
        print(f'{termColors.DANGER}$ python pydig.py <DOMAINS>{termColors.ENDC}')

def printDomainRecords(domains):
    for domain in domains:
        print(f'-- DOMAIN: {domain}')
        ip = dns.resolver.resolve(domain, 'A')
        print(f'IP: {ip[0].to_text()}')

        for rdata in dns.resolver.resolve(domain, 'NS'):
            print(f'NS: {rdata.target.to_text()}')

        fqn = domain if re.search('^www.', domain) else f'www.{domain}'
        for rdata in dns.resolver.resolve(fqn, 'CNAME'):
            print(f'CNAME: {rdata.target}')

def main():
    domains = argv[1:]

    validateArgs(domains)
    printDomainRecords(domains)

if __name__ == '__main__':
    main()

