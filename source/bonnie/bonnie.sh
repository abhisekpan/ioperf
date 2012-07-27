#!/usr/bin/env bash
mnt_dir=/mnt/nfs
mnt_options=tcp
server=65.123.202.103
exportdir=/mnt/nfsserver 
ramsize=16082
bonnie_user=bonnietest
if sudo mount | grep $mnt_dir > /dev/null; then
    sudo umount $mnt_dir
fi
sudo mount -t nfs -o $mnt_options $server:$exportdir $mnt_dir
ls $mnt_dir
#run bonnie
output_label=base
bonnie++ -d $mnt_dir -m $output_label -r $ramsize
