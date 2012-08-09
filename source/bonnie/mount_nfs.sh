#!/usr/bin/env bash
mnt_dir=/home
mnt_options=tcp
server=10.2.10.1
exportdir=/home 

if mount | grep $mnt_dir > /dev/null; then
    umount $mnt_dir
fi
mount -t nfs -o $mnt_options $server:$exportdir $mnt_dir
