#!/usr/bin/python
#
# Reads lijst_dieren_stripped* and extracts animal names
#
import re

dierendict = {}

filename1 = 'lijst_dieren1_stripped.htm'
filename2 = 'lijst_dieren2_stripped.htm'

file1 = open(filename1)
for line in file1:
    dierenmatch1 = re.search("(.)</span><span style=\"font-size: x-small;\">([^<]+)</span></a></li>",line)
    if dierenmatch1:
        dier = dierenmatch1.group(1).lower() + dierenmatch1.group(2).lower()
        dierendict[dier] = 'ole'
    else:
        dierenmatch2 = re.search(">([^<]+)</span></a></li>",line)
        if dierenmatch2:
            dier = dierenmatch2.group(1).lower()
            dierendict[dier] = 'ole'
        

file1.close()

file2 = open(filename2)
for line in file2:
    dierenmatch = re.search("_blank\">([^<]+)</a></td>",line)
    if dierenmatch:
        dier = dierenmatch.group(1).lower()
        print dier
        dierendict[dier] = 'ole'

file2.close()

bigfilename = 'alldieren.txt'
bigfile = open(bigfilename,'w')
for dier in sorted(dierendict):
    bigfile.write("%s\n" % dier)
bigfile.close()
