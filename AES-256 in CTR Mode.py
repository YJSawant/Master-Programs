from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter
import os

key = os.urandom(32)
def encrypt(iinput, key):
		iinput = iinput + b"\0" * (AES.block_size - len(iinput) % AES.block_size)
		count = Counter.new(128)
		start=time.clock()
        x=encryptor.encrypt(iinput)
        print (time.clock()-start)
        return x	
    
def decrypt(einput, key):
		count = Counter.new(128)
		start=time.clock()
        x=decryptor.decrypt(einput).rstrip(b"\0")
        print (time.clock()-start)
        return x
        
def fileops1KB():
        testfile="File1KB.txt"
        with open(testfile,"rb") as infile:
            inputtext = infile.read()
            enctext = encrypt(inputtext, key)   
                
        with open("Enc1KB" + ".enc", 'wb') as outfile:
            outfile.write(enctext)    
        
        with open("Enc1KB.enc","rb") as infile:
            outputtext = infile.read()
            dectext = decrypt(outputtext, key)
	
        with open("Dec1KB" + ".txt", 'wb') as outfile:
            outfile.write(dectext)
        
def fileops1MB():
        testfile="File1MB.txt"
        with open(testfile,"rb") as infile:
            inputtext = infile.read()
            enctext = encrypt(inputtext, key)   
                
        with open("Enc1MB" + ".enc", 'wb') as outfile:
            outfile.write(enctext)    
        
        with open("Enc1MB.enc","rb") as infile:
            outputtext = infile.read()
            dectext = decrypt(outputtext, key)
	
        with open("Dec1MB" + ".txt", 'wb') as outfile:
            outfile.write(dectext)
        
fileops1KB()
fileops1MB()
        
