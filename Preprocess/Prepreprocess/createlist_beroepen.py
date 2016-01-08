#!/usr/bin/python
#
# Reads lijst_beroepen_stripped* and extracts job names
#
import re

beroependict = {}

filename1 = 'lijst_beroepen1_stripped.htm'
filename2 = 'lijst_beroepen2_stripped.htm'
filename3 = 'lijst_beroepen3_stripped.htm'

file1 = open(filename1)
for line in file1:
    beroepenmatch = re.search("title=\"beroep (.*)\"",line)
    if beroepenmatch:
        beroepenlist = beroepenmatch.group(1).lower().split(", ")
        for beroep in beroepenlist:
            beroependict[beroep] = 'ole'

file1.close()

file2 = open(filename2)
for line in file2:
    beroepenmatch = re.search("\">(.*)</a></li>",line)
    if beroepenmatch:
        beroepenlist = beroepenmatch.group(1).lower().split(", ")
        for beroep in beroepenlist:
            beroependict[beroep] = 'ole'

file2.close()

file3 = open(filename3)
for line in file3:
    beroepenmatch = re.search("<h2>([^<]*)</h2>",line)
    if beroepenmatch:
        beroepenlist = beroepenmatch.group(1).lower().split(", ")
        for beroep in beroepenlist:
            beroependict[beroep] = 'ole'

file3.close()

bigfilename = 'allberoepen.txt'
bigfile = open(bigfilename,'w')
for beroep in sorted(beroependict):
    bigfile.write("%s\n" % beroep)
bigfile.close()
