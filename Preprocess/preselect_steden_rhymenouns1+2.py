from limerickfunctions import *

#print "reading..."
elex = read_elex('/vol/bigdata/corpora/elex1.1/lexdata/elex-1.1.txt')
steden = read_categories('Prepreprocess/allsteden_phonemes.txt')
nouns = read_categories('Prepreprocess/allnouns_phonemes.txt')
#print "...done"

stadnounmatches = {}

for noun in nouns:
    if syllablecount(nouns[noun]) == 2:
        for stad in steden:
            if (metre(steden[stad]) == 'su' or metre(steden[stad]) == 'suu') and rhymes(nouns[noun],steden[stad]):
                if not stad in stadnounmatches:
                    stadnounmatches[stad] = {}
                stadnounmatches[stad][noun] = 1

for stad in stadnounmatches:
    if len(stadnounmatches[stad]) > 1:
        for noun in stadnounmatches[stad]:
            print stad, noun


