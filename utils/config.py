#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys

def aria2load():
    config = {}
    fname = os.path.expanduser("~/.aria2/aria2.conf")
    for line in open(fname):
        line = line.rstrip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        (name, value) = line.split("=")
        name = name.strip()
        config[name] = value
    return config
