'''
Created on 28 oct. 2016

@author: Jordi Marsal

AES AddRound algorhitm

'''

from operator import xor

class AddRound:
    def __init__(self, clau, text, debug):
        self.clau=clau
        self.debug=debug
        self.out = []
        self.sigma=[]
        
        scale = len(clau)/2 
        num_of_bits = len(clau)*4 #cada parell de caracters de la clau es un num hex
        # master_bin = bin(int(clau, scale))[2:].zfill(num_of_bits)
        
        text_bin = bin(int(text, scale))[2:].zfill(num_of_bits)
        clau_bin = bin(int(clau, scale))[2:].zfill(num_of_bits)
        if debug:
            print (text_bin)
            print (len(text_bin))
            print (clau_bin)
            print (len(clau_bin))
        
        
        text_bin_estat = []
        for bit in range(1,num_of_bits+1):
            text_bin_estat.append(text_bin[bit-1])
        
        clau_bin_K = []
        for bit in range(1,num_of_bits+1):
            clau_bin_K.append(clau_bin[bit-1])
        
        if debug:    
            print ("text_bin_estat: "+str(text_bin_estat))
            print ("len text_bin_estat: "+str(len(text_bin_estat)))
        
        mat_text = self.matriu(text_bin, num_of_bits)
        mat_K = self.matriu(clau_bin, num_of_bits)
        
        
        self.printl("S:",mat_text)
        self.printl("K:",mat_K)
        
        mat_rounded= self.xor_mats(mat_text, mat_K)
        
        
        self.printl("Rounded:",mat_rounded)
        
        #hex_subkey = hex(int(subkey, 2))
        m_flat=[]
        for i in range(0,len(mat_rounded),4):
            for g in range(8):
                m_flat.append(str(mat_rounded[i][g])) 
        
        if debug:   
            print(m_flat)
        
        subkey = ""
        for bit in m_flat: 
            subkey += bit
        
        hex_subkey = hex(int(subkey, 2))
        if debug:
            print(hex_subkey)

        print("end")
    
    def xor_mats(self, mat1, mat2):
        mat_xor=[]
        
        for x in range(len(mat1)):
            linia=[]
            for y in range(8):
                a=int(mat1[x][y])
                b=int(mat2[x][y])
                c=xor(a, b)
                #print ("a:%s b:%s c:%s"% (str(a),str(b),c))
                linia.append(c)
            mat_xor.append(linia)
        return mat_xor
    
    def xorJ(self, a, b):
        if (a & b):
            c=0
        else:
            c=1
        return c
    
    def matriu(self, texte01, numBits):
        
        list01_ = []
        for bit in range(1,numBits+1):
            list01_.append(texte01[bit-1])
        
        mat_s=[]
        c=0
        for f in range(0,len(list01_),8):
            t=[]
            for g in range(8):
                #print("g: "+str(text_bin_estat[f+g]))
                t.append(texte01[f+g])
            #print("t: "+str(t))
            mat_s.append(t)
            c+=1
        return mat_s
    
    def printl(self,string, llista):
        print("#### %s ####"% (string))
        for i in range(len(llista)):
            print("%s: %s "% (i,str(llista[i])) )
        
    
        
        
        
key=      "b4b5c5542ee51f99d641778f7203015f"
key=      "C0A68D43E97C6D264D32341976C6B379"

plaintext="C8F614742B2430EAC6547F2F0FBBFF09"
plaintext="B7E31D15F5FE15957C41FB324D7C7C24"

a=AddRound(key, plaintext, False)


