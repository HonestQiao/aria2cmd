#!/bin/bash

curdir=$(dirname $(readlink -f $0))
fnotify="$curdir/utils/notify.py"
fsession="$curdir/date/session"

if [ ! -f $fsession ];then
    touch $fsession
fi

aria2c --on-download-complete="$fnotify" --on-bt-download-complete="$fnotify" --save-session="$fsession" --input-file="$fsession" --enable-rpc -D
