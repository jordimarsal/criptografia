'''
Created on 28 oct. 2016

@author: Jordi Marsal

DES: Initial permutation
'''
class per_ini:
    def __init__(self, blocM, debug):
        self.blocM=blocM
        self.debug=debug
        self.out = []
        self.sigma=[]
        sig=[]
        self.sigma = self.fillSigma(sig)
        
        scale = len(blocM) 
        num_of_bits = len(blocM)*4 #cada parell de caracters de la clau es un num hex
        master_bin = bin(int(blocM, scale))[2:].zfill(num_of_bits)
        
        #print (master_bin)
        #print (len(master_bin))
        
        bin_estat = []
        for bit in range(1,num_of_bits+1):
            bin_estat.append(master_bin[bit-1])
            
        #print ("bin_estat: "+str(bin_estat))
        #print ("len bin_estat: "+str(len(bin_estat)))
        
        subkey_after_SIGMA = []
        for bit in self.sigma:
            subkey_after_SIGMA.append(bin_estat[bit-1])
        
        subkey = ""
        for bit in subkey_after_SIGMA: 
            subkey += bit
        print("  permutacio:%s"% subkey)    
        print ("len(permutacio)= %s" % len(subkey))
        hex_subkey = hex(int(subkey, 2))
        hex_subkey= hex_subkey.upper()
        print ("Permutacio inicial : " + hex_subkey)
        
    
    def fillSigma(self, sig):
        sig=[58,50,42,34,26,18,10,2,
        60,52,44,36,28,20,12,4,
        62,54,46,38,30,22,14,6,
        64,56,48,40,32,24,16,8,
        57,49,41,33,25,17,9,1,
        59,51,43,35,27,19,11,3,
        61,53,45,37,29,21,13,5,
        63,55,47,39,31,23,15,7]
        print (sig)
        return sig
        
        

bloc="5151544543400x4c0x4f"
bloc="4953535545415349"
bloc="45414E444A555354"
per_ini(bloc, True)

     