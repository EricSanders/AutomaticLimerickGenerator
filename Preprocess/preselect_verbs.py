from limerickfunctions import *

#print "reading..."
elex = read_elex('/vol/bigdata/corpora/elex1.1/lexdata/elex-1.1.txt')
verbs = read_categories('Prepreprocess/allverbs_phonemes.txt')
#print "...done"

for verb in verbs:
    if (syllablecount(verbs[verb]) < 3):
        print verb


