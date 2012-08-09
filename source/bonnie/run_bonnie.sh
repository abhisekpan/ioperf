#!/usr/bin/env bash
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 2048:1024 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_2G_1K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_2G_1K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 2048:4096 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_2G_4K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_2G_4K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 2048:16384 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_2G_16K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_2G_16K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 2048:65536 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_2G_64K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_2G_64K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 2048:262144 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_2G_256K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_2G_256K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 2048:524288 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_2G_512K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_2G_512K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 2048:1048576 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_2G_1024K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_2G_1024K_20.txt
echo "===================================================================="
echo "===================================================================="

/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 4096:1024 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_4G_1K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_4G_1K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 4096:4096 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_4G_4K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_4G_4K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 4096:16384 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_4G_16K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_4G_16K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 4096:65536 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_4G_64K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_4G_64K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 4096:262144 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_4G_256K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_4G_256K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 4096:524288 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_4G_512K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_4G_512K_20.txt
echo "===================================================================="
echo "===================================================================="
/home/apan/bonnieroot/sbin/bonnie++ -d /tmp/bonniedir -s 4096:1048576 -n 20 -m `hostname` -u apan:apan -q -f -x 20 > /home/apan/bonnieout/uv_local_buffered_4G_1024K_20.txt
/home/apan/ioperf/source/format_out.py < /home/apan/bonnieout/uv_local_buffered_4G_1024K_20.txt
echo "===================================================================="
echo "===================================================================="

#| /home/apan/bonnieroot/bin/bon_csv2html > ./bonnieout/uv_local_2G_direct.html
