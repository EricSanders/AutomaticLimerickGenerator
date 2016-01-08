#!/usr/bin/python
import sys, getopt
import limerick

beroep = ''
stad = ''

opts, args = getopt.getopt(sys.argv[1:],"b:d:s:l:",["beroep=","dier=","stad=","land="])

for opt, arg in opts:
    if opt in ("-b", "--beroep"):
        beroep = arg
    elif opt in ("-d", "--dier"):
        dier = arg
    elif opt in ("-s", "--stad"):
        stad = arg
    elif opt in ("-l", "--land"):
        land = arg

mylimerick = limerick.limerick()

#mylimerick.rhymes('geloven','verkopen')
mylimerick.create(argberoep=beroep,argstad=stad)
#mylimerick.create(stad='delden')
#print "yoyoyo"

