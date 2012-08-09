#! /usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import csv
import sys
import fileinput
#try:
#    in_filename = sys.argv[1]
#except IndexError:
#    in_filename = sys.stdin
#relevant columns
relevant_cols = [2,	#host
    5,	#File Size (GB)
    19,	#Num Files
    6,	#Block Size(KB)
    9,	#Block Write (K/sec)
    11,	#Block Rewrite (K/sec)
    15,	#Block Read (K/sec)
    17,	#Random Seek (/sec)
    24,	#Seq Create (/sec)
    28,	#Seq Delete (/sec)
    31,	#Random Create (/sec)
    34]	#Random Delete (/sec)

reader = csv.reader(fileinput.input())
try:
    for row in reader:
        outlist = [row[i] for i in xrange(len(row)) if i in relevant_cols]
        csv.writer(sys.stdout).writerow(outlist)
except csv.Error, e:
    sys.exit('file %s, line %d: %s' % (fileinput.filename(), reader.line_num, e))

#input = sys.stdin.readline().split(',')
#sys.stdout.write(input)
#for i in xrange(len(input)):
#    print i, input[i]
