from limerickfunctions import *

#print "reading..."
elex = read_elex('/vol/bigdata/corpora/elex1.1/lexdata/elex-1.1.txt')
beroepen = read_categories('Prepreprocess/allberoepen_phonemes.txt')
#print "...done"

for beroep in beroepen:
    if (metre(beroepen[beroep]) == 'su'):
        print beroep


