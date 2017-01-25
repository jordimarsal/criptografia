'''
Created on 18 nov. 2016

@author: Jordi Marsal

Fast module exponentiation

2 classes to choose, exp2 is better for high numbers
'''

class exprap:
    def __init__(self, base, exponent, modul, debug=False):
        self.base=base
        self.exponent=exponent 
        self.modul=modul
        self.debug=debug
        self.c = self.doExpRap(base, exponent, modul)
        self.printC()

    def doExpRap(self, base, exponent, modul):
        c1=1
        for _ in range(exponent):
            c1 = (c1*base) % modul
        return c1
    
    def printC(self):
        print "##########################"
        print (" %i^%i mod %i = %i" % (self.base,self.exponent,self.modul,self.c))
        print "##########################"
        
class exp2:
    def __init__(self, base, exponent, modul,prin=True, debug=False):# Base, Exponent, Modul, boolPrint, boolDebug
        self.base = base
        self.exponent = exponent
        self.e = [x for x in bin(exponent)[2:]]
        if debug: print self.e
        self.modul=modul
        self.debug=debug
        self.prin=prin
        self.c = self.doExp2(base, exponent, modul)
        if prin:self.printC()

    def doExp2(self, base, exponent, modul):
        exp = self.e[::-1]
        res=1
        if self.debug: print "res ini:"+str(res),"."
        for i in exp:
            if self.debug: print "i:"+ i
            if int(i)==1:
                res =  (res * base) % modul 
                if self.debug: 
                    print "base:"+str(base)
                    print "res:"+str(res),"."
            base = base * base
        return res
    
    def printC(self):
        print "##########################"
        print (" %i^%i mod %i = %i" % (self.base,self.exponent,self.modul,self.c))
        print "##########################"
        
    def getC(self):
        return self.c
       
        
e1=exprap(4,13,497)

e2=exp2(4,13,497)


