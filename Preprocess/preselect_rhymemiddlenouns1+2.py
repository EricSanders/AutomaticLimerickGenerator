from limerickfunctions import *

#print "reading..."
elex = read_elex('/vol/bigdata/corpora/elex1.1/lexdata/elex-1.1.txt')
nouns = read_categories('Prepreprocess/allnouns_phonemes.txt')
#print "...done"

nounkeys = nouns.keys()
nounmatches = {}

for i in range(len(nounkeys)):
    noun1 = nounkeys[i]
    if syllablecount(nouns[noun1]) == 2:
        for j in range(i,len(nounkeys)):
            noun2 = nounkeys[j]
            if syllablecount(nouns[noun2]) == 2:
                if (rhymes(nouns[noun1],nouns[noun2])):
                    if not noun1 in nounmatches:
                        nounmatches[noun1] = {}
                    nounmatches[noun1][noun2] = 1

for noun1 in nounmatches:
    for noun2 in nounmatches[noun1]:
            print noun1, noun2


