#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os, subprocess
import xmlrpc

def remove(aria, gid):
    cmd = "getFiles('%s')" %(gid)
    uri = aria.abstract(cmd)[0]["uris"][0]["uri"]

    fsession = os.path.realpath(os.path.join(os.path.dirname(__file__), "../date/session"))
    result ="" 

    infile = open(fsession, 'r')
    for line in infile:
        if not uri in line:
            result = result + line 
    infile.close()

    outfile = open(fsession, "w") 
    outfile.write(result)
    outfile.close()

def main():
    gid=sys.argv[1]
    fname=os.path.basename(sys.argv[3])
    aria = xmlrpc.aria2ctl()
    remove(aria, gid)
    subprocess.call(["notify-send","Download Finish","%s" %(fname)])

if __name__ == '__main__':
    main()
