"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
import socket
import os
import sys

port = 21
banner = "FreeFloat FTP Server"

portList = [21, 22, 80, 110]
portOpen = True

services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def checkVulns(banner, filename):
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '[+] Server is vulnerable: ' + banner.strip('\n')


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-] ' + filename + ' does not exist.'
            exit(0)
        if not os.access(filename, os.R_OK):
            print '[-] ' + filename + ' access denied.'
            exit(0)
    else:
        print '[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>'
        exit(0)

    portList = [21, 22, 25, 80, 110, 443]
    for x in range(147, 150):
        ip = '192.168.95.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print '[+] ' + ip + ': ' + banner
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()