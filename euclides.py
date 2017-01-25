#coding: utf-8
'''
Created on 18 nov. 2016

@author: Jordi Marsal
'''
#############################
# mcd Euclides segons divisió
#############################
class mcd:
    def __init__(self, a, n, debug=False):
        self.a=a
        self.n=n
        self.debug=debug
        self.resul =[]
        self.c = self.mcd2(a,n)
        
    def mcd(self,a,n):
        while n != 0:
            t = n
            n = a % n
            a = t
        return a
    
    def mcd2(self,a,n):
        while n != 0:
            a, n = n, a % n
        return a
    
    def printC(self):
        print ("  mcd(%i,%i) = %i" % (self.a,self.n,self.n))
        
    def getC(self):
        return self.c


#####################################
# invers de a modul n quan mcd(a,n)=1 
# és a dir: a·x mod n = 1 , es troba la x
# (Euclides extés)
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
#####################################

class inv:
    def __init__(self, a, n, debug=False):
        self.a=a
        self.n=n
        self.debug=debug
        self.c = self.inv(a,n)
        
    def inv(self,a,n):
        t = 0;     newt = 1;    
        r = n;     newr = a;    
        while newr != 0:
            quotient = r / newr
            (t, newt) = (newt, t - quotient * newt) 
            (r, newr) = (newr, r - quotient * newr)
        if r > 1 : return "a is not invertible"
        if t < 0 : t = t + n
        return t
    
    def getC(self):
        return self.c
    
    def printC(self):
        print ("  %i^%i mod %i = %i" % (self.a,self.c,self.n,1))
        
#####################################
# 
##
# mcd
a = 46927
b = 39423
mcd1=mcd(a,b)
mcd1.printC()

# inverse mod:
i1=inv(7,15)
i1.printC()
