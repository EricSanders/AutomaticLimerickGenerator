from limerickfunctions import *

#print "reading..."
elex = read_elex('/vol/bigdata/corpora/elex1.1/lexdata/elex-1.1.txt')
middlenouns = read_categories('Prepreprocess/allnouns_phonemes.txt')
#print "...done"

for middlenoun in middlenouns:
    if (syllablecount(middlenouns[middlenoun]) < 3):
        print middlenoun


