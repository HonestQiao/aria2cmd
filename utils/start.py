#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os
import xmlrpc

def add(aria, gid):
    cmd = "getFiles('%s')" %(gid)
    uri = aria.abstract(cmd)[0]["uris"][0]["uri"]
    
    fsession = os.path.realpath(os.path.join(os.path.dirname(__file__), "../date/session"))
    f = open(fsession, 'a')
    f.write(uri)
    f.write("\n")
    f.close()

def main():
    gid=sys.argv[1]
    aria = xmlrpc.aria2ctl()
    add(aria, gid)

if __name__ == '__main__':
    main()
