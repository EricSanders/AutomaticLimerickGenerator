def rhymes(phon1,phon2):
    vowels = ['I','E','A','O','Y','i','y','e','2','a','o','u','@']
    if phon1 == phon2:
        return(0)
    
    if phon1 and phon2:
        stress1 = 0
        stress2 = 0
        syllables1 = phon1.split('-')
        nrsyllables1 = len(syllables1)
        for i in range(nrsyllables1-1):
            if syllables1[i][0] == '\'':
                stress1 = i
        syllables2 = phon2.split('-')
        nrsyllables2 = len(syllables2)
        for i in range(nrsyllables2-1):
            if syllables2[i][0] == '\'':
                stress2 = i
        if nrsyllables1-stress1 != nrsyllables2-stress2:
            #                print 'stress error'
            return(0)
        else:
            for vowel in vowels:
                placevowel1 = syllables1[stress1].find(vowel)
                placevowel2 = syllables2[stress2].find(vowel)
                if placevowel1 >=0 and placevowel2 >= 0:
                    if not syllables1[stress1][placevowel1:] == syllables2[stress2][placevowel2:]:
                        #                            print 'rhyme error in stressed syllable'
                        return(0)
                    else:
                        rhymeerror = 0
                        for j in range(nrsyllables1-stress1-1):
                            if not syllables1[stress1+j+1] == syllables2[stress2+j+1]:
                                rhymeerror = 1
                            #                                    print 'rhyme error in unstressed syllable'
                        if not rhymeerror:
                            #                                print word1 +' rhymes '+word2
                            return(1)
                elif placevowel1 >=0 or placevowel2 >= 0:
                    #                        print 'nucleus error'
                    return(0)

def metre(phon):
    metre = ''

    syllables = phon.split('-')
    for syllable in syllables:
        if syllable[0] == '\'':
            metre += 's'
        else:
            metre += 'u'
    return metre

def syllablecount(phon):
    syllablecount = 0

    syllables = phon.split('-')
    syllablecount = len(syllables)
    return syllablecount

def read_elex(elexname):
    elexdict = {}
    elex = open(elexname)
    for line in elex:
        fields = line.split('\\')
        ort = fields[8].lower()
        pos = fields[9]
        phon = fields[15]
        elexdict[ort] = phon
    elex.close()
    return elexdict

def read_categories(filename):
    words = {}
    file = open(filename)
    for line in file:
        line = line.rstrip('\r\n')
        fields = line.split('\t')
#            print fields[0]+'=>'+fields[1]
        words[fields[0]] = fields[1]
    file.close()
    return(words)
