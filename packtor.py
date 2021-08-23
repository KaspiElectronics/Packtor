import random
import json
from sys import argv

words = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x", "y","z",
    "0","1","2","3","4","5","6","7","8","9",
    "~","`","!","@","#","$","%","^","&","*","(",")","-","_",
    "=","+","?","/",".",">","<",",","\\","'","\"",";",":","\n"
]

words_t = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x", "y","z",
    "0","1","2","3","4","5","6","7","8","9",
    "~","`","!","@","#","$","%","^","&","*","(",")","-","_",
    "=","+","?","/",".",">","<",",","\\","'","\"",";",":","\n"
]
algorithm = {}
algorithm_decrypt = {}

# init new packtor algorithm
def init():
    # shuffle words
    for i in range(len(words)-1,0,-1):
        j = random.randint(0,i+1)
        words_t[i],words_t[j] = words_t[j],words_t[i]

    # create encryption alogorithm
    for i in range(len(words)):
        algorithm[words[i]] = words_t[i]
    
    # create decryption alogorithm
    for i in range(len(words)):
        algorithm_decrypt[words_t[i]] = words[i]

    # write alogorithms to json files
    json_object = json.dumps(algorithm,indent=4)
    with open("algorithm.json","w") as file :
        file.write(str(json_object))
    json_object = json.dumps(algorithm_decrypt,indent=4)
    with open("algorithm_decrypt.json","w") as file :
        file.write(str(json_object))

# packtor decryptor
def decrypt(text,file=False) :
    input = text
    # read algorithm
    fin_algo = open("algorithm_decrypt.json",)
    algorithm = json.load(fin_algo)

    # check if we want to decrypt a file
    if file : 
        with open(text) as fin :
            input = fin.read()

    # decrypt input 
    output = ""
    for t in input:
        if not t in words :output += t
        else :output += algorithm[t]

    # write decryption data to a file
    with open("cache/output_decrypt.txt","w") as fout :
        fout.write(output) 

    return output  

# packtor encryptor
def encrypt(text,file=False):
    input = text
    # read algorithm
    fin_algo = open("algorithm.json",)
    algorithm = json.load(fin_algo)

    # check if we want to decrypt a file
    if file : 
        with open(text) as fin :
            input = fin.read()

    # encrypt input 
    output = ""
    for t in input : 
        if not t in words :output += t
        else : output += algorithm[t]

    # write encryption data to a file
    with open("cache/output_encrypt.txt","w") as fout :
        fout.write(output)
    
    return output
    
if __name__ == "__main__" :
    if len(argv) < 2 :pass
    elif len(argv) == 2 and argv[1] == "init" :init()
    elif len(argv) == 3 and argv[1] == "encryptf" :print(encrypt(argv[2],file=True))
    elif len(argv) == 3 and argv[1] == "encrypt" :print(encrypt(argv[2]))
    elif len(argv) == 3 and argv[1] == "decryptf" :print(decrypt(argv[2],file=True))
    elif len(argv) == 3 and argv[1] == "decrypt" :print(decrypt(argv[2]))
