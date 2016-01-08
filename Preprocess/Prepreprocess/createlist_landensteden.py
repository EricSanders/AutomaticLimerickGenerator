#!/usr/bin/python
#
# Reads lijst_steden_stripped* and extracts job names
#
import re

stedendict = {}
landendict = {}

filename1 = 'lijst_steden1_stripped.htm'
filename2 = 'lijst_steden2_stripped.htm'

file1 = open(filename1)
for line in file1:
    stedenmatch = re.findall("\">([^<]*)</a>",line)
    if stedenmatch:
        for stad in stedenmatch:
#            print stad.lower()
            stedendict[stad.lower()] = 'ole'

file1.close()

file2 = open(filename2)
for line in file2:
    landenstedenmatch = re.search(">([^<]*)</a>.+>([^<]*)</a></li>",line)
    if landenstedenmatch:
        land = landenstedenmatch.group(1).lower()
        sted = landenstedenmatch.group(2).lower()
#        print land
        landendict[land] = 'ole'
        stedendict[stad] = 'ole'

file2.close()

bigfilename = 'allsteden.txt'
bigfile = open(bigfilename,'w')
for stad in sorted(stedendict):
    bigfile.write("%s\n" % stad)
bigfile.close()

bigfilename = 'alllanden.txt'
bigfile = open(bigfilename,'w')
for land in sorted(landendict):
    bigfile.write("%s\n" % land)
bigfile.close()
