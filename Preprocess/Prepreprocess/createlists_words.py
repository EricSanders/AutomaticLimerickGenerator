#!/usr/bin/python
#
# Creates lists according to pos
#

nouns = {}
verbs = {}
prepos = {}

elexname = 'elex-1.1.txt'

elex = open(elexname)
for line in elex:
    fields = line.split('\\')
    ort = fields[8].lower()
    pos = fields[9]
    phon = fields[15]
    if pos == 'WW(pv,verl,ev)':
        verbs[ort] = phon
    elif pos == 'N(soort,ev,basis,zijd,stan)':
        nouns[ort] = phon
    elif pos == 'VZ(init)':
        prepos[ort] = phon
elex.close()

file = open('allnouns_phonemes.txt','w')
for ort in nouns:
    file.write("%s\t%s\n" % (ort, nouns[ort]))
file.close()

file = open('allverbs_phonemes.txt','w')
for ort in verbs:
    file.write("%s\t%s\n" % (ort, verbs[ort]))
file.close()

file = open('allprepos_phonemes.txt','w')
for ort in prepos:
    file.write("%s\t%s\n" % (ort, prepos[ort]))
file.close()

