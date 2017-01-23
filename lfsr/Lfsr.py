#coding: utf-8
'''
Created on 27 oct. 2016

@author: Jordi Marsal
'''
from operator import xor

# polinomi: termeindepe+x^1+x^2+..x^n
class lsfr:
    def __init__(self, polinomi, inici, iteracions, debug):
        self.polinomi=polinomi
        self.inici=inici 
        self.iteracions=iteracions
        self.debug=debug
        self.out = []
        self.lsfr(polinomi, inici, iteracions)

    def doIteration(self, poli, lido):
        resXO = self.getXO(poli, lido)
        self.out.append(lido[len(lido)-1])
        lido = self.displace(resXO, lido)
        return lido
    
    def displace(self, xo, lido):
        for index in range(len(lido)):
            i=len(lido)-(index+1)
            if(index<(len(lido)-1)):lido[i]=lido[i-1]
        lido[0]=xo
        return lido
    
    # implementacio de xor segons polinomi 
    def getXO(self, pol, lixo):
        lop = pol[::-1]
        xoli=lixo[::-1] # reverse list
        if self.debug: print("cells: "+str(lixo))
        xo = 2
        for index, item in enumerate(xoli):
            if (index==0):
                xo=xoli[0]
                if self.debug:print("    xo(inicial):%s"% (xo) )
            if (index>0):
                if self.debug:print("    iter[%s]: x^%s, cell:%s, xo(pre):%s"% (str(index), str((len(pol)-index)), str(item),str(xo)))
                if (lop[index]==1): 
                    xo=xor(item, xo)
                elif self.debug:print("    NOT XOR")
                if self.debug:print("               xo(post):%s"% (xo) )
        return xo
    
    def lsfr(self, polinomi, inici, iteracions):
        linici,pol=[],[]
        for f in range(len(inici)):
            linici.append(int(inici[f]))
        for f in range(len(polinomi)):
            pol.append(int(polinomi[f]))
        if self.debug:print("pol: "+str(pol))
        if self.debug:print("ini: "+str(linici))
        for f in range(iteracions): 
            if self.debug:print("f:%s"% f)
            linici=self.doIteration(pol, linici)
            if self.debug:print("  li:"+str(linici))
        if self.debug:print("###############################")
        if self.debug:print("out: "+str(self.out))
        if self.debug:print("###############################")
        
    def listOut(self):
        return self.out
    
    def getComplexitat(self):
        return (len(self.inici))
    
    def getPeriode(self):
        n=len(self.inici)
        return (2**n)-1


# polinomi: termeindepe+x^1+x^2+..x^n

 
l=lsfr("111011", "01100", 36, False)
l1=l.listOut()
print l1

l2=lsfr("101111", "10101", 10, False)

l3=lsfr("1011111111101", "111110111110", 12, False)
#print ("complexitat linial: "+str(l3.getComplexitat()))
#print ("periode: "+str(l3.getPeriode()))

#Prac2 pregunta 1 i única
Prac2P1d=lsfr("1000011", "000011", 12, False)
#print Prac2P1d.listOut()
Prac2P1c=lsfr("1110011", "000011", 12, False)
#print Prac2P1c.listOut()

#PAC 2 - Flux
# P1
Pac2P1=lsfr("111101", "10001", 10, False)
print ("Pregunta 1: "+str(Pac2P1.listOut()))

# P2
Pac2P2=lsfr("1011111111101", "111110111110", 12, False)
print ("\nP2: complexitat linial: "+str(Pac2P2.getComplexitat()))
print ("P2: periode: "+str(Pac2P2.getPeriode()))

#P3
Pac2P3b=lsfr("11111", "1011", 8, False)
print ("\nPregunta 3b: "+str(Pac2P3b.listOut()))
Pac2P3d=lsfr("10011", "1011", 8, False)
print ("Pregunta 3d: "+str(Pac2P3d.listOut()))
Pac2P3e=lsfr("11001", "1011", 8, False)
print ("Pregunta 3e: "+str(Pac2P3e.listOut()))


Prac2P3=lsfr("1110110000010000000", "0100100101010101010", 40, False)
print ("\nPrac2 P3: complexitat linial: "+str(Prac2P3.getComplexitat()))
print ("Prac2 P3: periode: "+str(Prac2P3.getPeriode()))
print ("P3: "+str(Prac2P3.listOut()))