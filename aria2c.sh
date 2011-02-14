#!/bin/bash

curdir=$(dirname $(readlink -f $0))
fstart="$curdir/utils/start.py"
fcomplete="$curdir/utils/complete.py"
finput="$curdir/date/session"

if [ ! -f $finput ];then
    touch $finput
fi

aria2c --on-download-start="$fstart" --on-download-complete="$fcomplete" --on-bt-download-complete="$fcomplete" --input-file="$finput" --enable-xml-rpc -D
