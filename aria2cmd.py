#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse, sys, os, cmd
from subprocess import Popen, PIPE
from pprint import pprint
from utils import xmlrpc, complete

class interactive(cmd.Cmd):
    def __init__(self, aria):
        self.aria = aria
        cmd.Cmd.__init__(self)
        self.intro = "Welcome to aria2cmd interactive mode. Type help for available command."

    def printlist(self, query):
        row, column = Popen("stty size",shell=True, stdout=PIPE).communicate()[0].split()
        width = [4,0,14,10,10,5]
        width[1] = int(column)-width[0]-width[2]-width[3]-width[4]-width[5]-6
        fmt = "%-*s|%-*s|%-*s|%-*s|%-*s|%-*s"

        print "=" * int(column)
        print fmt %(width[0],"GID",
                    width[1],"File",
                    width[2],"Process",
                    width[3],"Down",
                    width[4],"UP",
                    width[5],"SEED")
        print "-" * int(column)

        num = len(query)
        for i in range(num):
            print fmt %(width[0],query[i]["gid"],
                        width[1],query[i]["file"][:width[1]-1],
                        width[2],query[i]["length"]+"("+query[i]["ratio"]+")",
                        width[3],query[i]["down"],
                        width[4],query[i]["up"],
                        width[5],query[i]["seed"])

        print "=" * int(column)

    def ps(self, rtcode):
        if type(rtcode).__name__ == "tuple":
            print "Fail. %s" %(rtcode[1])
    
    def helpinfo(self):
        print '''Command Summary:
        
        add URI         add a uri to download
        ls [STATUS]     list all downloads in one STATUS.
                        valid status are: active, wait, stop. default is active
        rm GID          remove a download
        stop [GID]      stop a download, or all download if no GID is given
        start [GID]     start a download, or all download if no GID is given
        clear           clear screen

        You can also run arbitrary aria2c xml-rpc command, such as:
        tellStatus("1")'''

    def do_help(self, argv):
        '''help [command]: Print help information'''
        if not argv:
            self.helpinfo()
        cmd.Cmd.do_help(self, argv)

    def do_clear(self, argv):
        '''clear: clear the screen'''
        os.system("clear")

    def do_add(self, argv):
        '''add URI: add a URI to download'''
        if argv:
            rtcode = self.aria.add(argv)
        else:
            rtcode = (False, "No URI given")
        self.ps(rtcode)

    def do_ls(self, argv):
        '''ls [STATUS]: list all downloads in one STATUS.valid status are: active, wait, stop. default is active'''
        if argv == "wait":
            query = self.aria.tell("wait")
        elif argv == "stop":
            query = self.aria.tell("stop")
        else:
            query = self.aria.tell("active")

        if type(query).__name__ != "tuple":
            self.printlist(query)
        else:
            self.ps(query)

    def do_rm(self, argv):
        '''rm GID: remove a download'''
        if argv:
            try:
                complete.remove(self.aria, argv)
            except:
                pass
            rtcode = self.aria.remove(argv)
        else:
            rtcode = (False, "No GID given")
        self.ps(rtcode)
        
    def do_stop(self, argv):
        '''stop [GID]: stop a download, or all download if no GID is given'''
        self.ps(self.aria.stop(argv))

    def do_start(self, argv):
        '''start [GID]: start a download, or all download if no GID is given'''
        self.ps(self.aria.start(argv))
    
    def default(self, argv):
        result = self.aria.abstract(argv)
        if type(result).__name__ != "tuple":
            try:
                pprint(result)
            except Exception as e:
                print "Fail. %s" %(e)
        else:
            self.ps(result)

def main():
    aria = xmlrpc.aria2ctl()

    if len(sys.argv) == 1:
        try:
            interactive(aria).cmdloop()
        except KeyboardInterrupt:
            print
            sys.exit(0)
    else:
        parser = argparse.ArgumentParser(description="Control aria2c xml-rpc in terminal")
        parser.add_argument("-c", dest="cmd", nargs="?", help="Run an internal command")
        args = parser.parse_args()
        cmd = args.cmd
        interactive(aria).onecmd(cmd)

if __name__ == '__main__':
    main()
