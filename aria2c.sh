#!/bin/bash

curdir=$(dirname $(readlink -f $0))
fnotify="$curdir/utils/notify.py"
fsession="$curdir/date/session"

if [ ! -f $finput ];then
    touch $finput
fi

aria2c --on-download-complete="$fnotify" --on-bt-download-complete="$fnotify" --save-session="$fsession" --input-file="$fsession" --enable-xml-rpc -D
