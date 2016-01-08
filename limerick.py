import random

class limerick:
    beroepen = []
    steden_rhymnouns = {}
    steden = []
    rhymemiddlenouns = {}
    rhymemiddlenouns1 = []
    middlenouns = []
    verbs1 = []
    verbs2 = []
    verbs3_4 = []

    def __init__(self):
         self.beroepen = self.read_categories1('Preprocess/beroepen.txt')
         self.steden_rhymenouns = self.read_categories2('Preprocess/steden_rhymenouns1+2.txt')
#         self.steden = self.steden_rhymenouns.keys()
         self.rhymemiddlenouns = self.read_categories2('Preprocess/rhymemiddlenouns1+2.txt')
#         self.rhymemiddlenouns1 = self.rhymemiddlenouns.keys()
         self.middlenouns = self.read_categories1('Preprocess/middlenouns1+2.txt')
         self.verbs1 = self.read_categories1('Preprocess/verbs1.txt')
         self.verbs2 = self.read_categories1('Preprocess/verbs2.txt')
         self.verbs3_4 = self.read_categories1('Preprocess/verbs3+4.txt')

    def create(self,argberoep='',argstad=''):
        
        beroep = ''
        stad = ''
        rhymenoun1 = ''
        rhymenoun2 = ''
        rhymemiddlenoun1 = ''
        rhymemiddlenoun2 = ''
        middlenoun1 = ''
        middlenoun2 = ''
        verb1 = ''
        verb2 = ''
        verb3 = ''
        verb4 = ''

        if argberoep in self.beroepen:
            beroep = argberoep
        else:
            beroep = random.choice(self.beroepen)

        if argstad in self.steden_rhymenouns.keys():
            stad = argstad
        else:
            stad = random.choice(self.steden_rhymenouns.keys())

        rhymenoun1 = self.steden_rhymenouns[stad].pop(random.randint(0,len(self.steden_rhymenouns[stad])-1))
        rhymenoun2 = self.steden_rhymenouns[stad].pop(random.randint(0,len(self.steden_rhymenouns[stad])-1))

        rhymemiddlenoun1 = random.choice(self.rhymemiddlenouns.keys())
        rhymemiddlenoun2 = self.rhymemiddlenouns[rhymemiddlenoun1].pop(random.randint(0,len(self.rhymemiddlenouns[rhymemiddlenoun1])-1))

 #       verb1 = self.verbs1.pop(random.randint(0,len(self.verbs1)-1))
        verb1 = random.choice(self.verbs1)
 #       verb2 = self.verbs2.pop(random.randint(0,len(self.verbs2)-1))
        verb2 = random.choice(self.verbs2)
        verb3 = self.verbs3_4.pop(random.randint(0,len(self.verbs3_4)-1))
        verb4 = self.verbs3_4.pop(random.randint(0,len(self.verbs3_4)-1))

        middlenoun1 = self.middlenouns.pop(random.randint(0,len(self.middlenouns)-1))
        middlenoun2 = self.middlenouns.pop(random.randint(0,len(self.middlenouns)-1))

        if argberoep and not argberoep == beroep:
            print 'sorry, '+argberoep+' kon niet gebruikt worden<br>&nbsp;<br>'
        if argstad and not argstad == stad:
            print 'sorry, '+argstad+' kon niet gebruikt worden<br>&nbsp;<br>'

        print 'er was eens een '+beroep+' uit '+stad+'<br>'
        print 'die '+verb1+' zijn '+middlenoun1+' de '+rhymenoun1+'<br>'
        print 'toen '+verb2+' er een '+rhymemiddlenoun1+'<br>'
        print 'die '+verb3+' een '+rhymemiddlenoun2+'<br>'
        print 'en '+verb4+' de '+middlenoun2+' de '+rhymenoun2+'<br>'

    def read_categories1(self,filename):
        file = open(filename)
        words = []
        for line in file:
            line = line.rstrip('\r\n')
            words.append(line)
        file.close()
        return(words)

    def read_categories2(self,filename):
        file = open(filename)
        words = {}
        for line in file:
            line = line.rstrip('\r\n')
            fields = line.split(' ')
            if fields[0] not in words:
                words[fields[0]] = []
            words[fields[0]].append(fields[1])
        file.close()
        return(words)
