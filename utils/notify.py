#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os, subprocess

def main():
    fname=os.path.basename(sys.argv[3])
    subprocess.call(["notify-send","Download Finish","%s" %(fname)])

if __name__ == '__main__':
    main()
