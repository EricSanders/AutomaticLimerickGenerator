#!/usr/bin/python
#
# Finds phonemic transcriptions of lists in elex
#

elexdict = {}

elexname = 'elex-1.1.txt'

elex = open(elexname)
for line in elex:
    fields = line.split('\\')
    ort = fields[8].lower()
    phon = fields[15]
#    print ort + ' => ' + phon
    elexdict[ort] = phon
elex.close()

lijstberoepenname = 'allberoepen.txt'
lijstdierenname = 'alldieren.txt'
lijstlandenname = 'alllanden.txt'
lijststedenname = 'allsteden.txt'

lijstberoepenname_phonemes = 'allberoepen_phonemes.txt'
lijstdierenname_phonemes = 'alldieren_phonemes.txt'
lijstlandenname_phonemes = 'alllanden_phonemes.txt'
lijststedenname_phonemes = 'allsteden_phonemes.txt'

lijstberoepen = open(lijstberoepenname)
lijstberoepen_phonemes = open(lijstberoepenname_phonemes,'w')
for line in lijstberoepen:
    word = line.strip()
    if word in elexdict:
        lijstberoepen_phonemes.write("%s\t%s\n" % (word , elexdict[word]))
#        print word  + ' => ' + elexdict[word]
#    else:
#        print word + ' not in dict'

lijstdieren = open(lijstdierenname)
lijstdieren_phonemes = open(lijstdierenname_phonemes,'w')
for line in lijstdieren:
    word = line.strip()
    if word in elexdict:
        lijstdieren_phonemes.write("%s\t%s\n" % (word , elexdict[word]))
#        print word  + ' => ' + elexdict[word]
#    else:
#        print word + ' not in dict'

lijstlanden = open(lijstlandenname)
lijstlanden_phonemes = open(lijstlandenname_phonemes,'w')
for line in lijstlanden:
    word = line.strip()
    if word in elexdict:
        lijstlanden_phonemes.write("%s\t%s\n" % (word , elexdict[word]))
#        print word  + ' => ' + elexdict[word]
#    else:
#        print word + ' not in dict'

lijststeden = open(lijststedenname)
lijststeden_phonemes = open(lijststedenname_phonemes,'w')
for line in lijststeden:
    word = line.strip()
    if word in elexdict:
        lijststeden_phonemes.write("%s\t%s\n" % (word , elexdict[word]))
#        print word  + ' => ' + elexdict[word]
#    else:
#        print word + ' not in dict'

