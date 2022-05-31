import numpy as np

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def flatten(t):
    return [item for sublist in t for item in sublist]
def rank_simple(l):
    return [sorted(l).index(x) for x in l]

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def encipher(text,key):
    
 text = text.upper().replace(" ", "")
 key = key.upper()
 vlist= Convert(text)
 keylist =[]
 for char in key:
    if char not in keylist:
        keylist.append(char)
 
 keyord =[]

 for char in keylist:
     num = ord(char)-65
     keyord.append(num)

 keyord = rank_simple(keyord)
 perm =[]
 for i in range(0,len(keyord)):
     perm.append(keyord.index(i)) 
 n = len(keylist)
 klist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
          'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
 templ = []
 for letter in klist:
    if letter not in vlist:
        templ.append(letter)
        
 vlist.extend(templ)
 vlist = chunks(vlist,n)
 for i in vlist:
     if len(i) < n:
         a = [0]*(n-len(i))
         i.extend(a)
 
 array = np.array(vlist)
 array = array[:, perm]  

 num_columns = np.shape(array)[1]
 l = []
 for i in range(0,num_columns):  
     l.append(array[:,i].tolist())
 
 l = flatten(l)
 l = ''.join(map(str, l))
 return l

def decipher(text, key):
 key = key.upper()
 keylist =[]
 for char in key:
    if char not in keylist:
        keylist.append(char)
        
 darray= np.array(chunks(Convert(text), int(len(text)/len(keylist))))
 darray = darray.transpose()
 
 keyord =[]

 for char in keylist:
     num = ord(char)-65
     keyord.append(num)
 keyord = rank_simple(keyord)
 darray = darray[:, keyord] 
 l1 = flatten(darray[:].tolist())
 l1 = ''.join(map(str, l1))
 return l1

#CNKRFQZTSLHGV0AOEDBMYIPUWJX0
msg = "Actions Speak Louder than words"
key = "college"
print("Plaintext is: "+msg)
print("\nThe key is: "+key)
enc = encipher(encipher(msg, key),key)
enc1 = enc.replace("0", '')
print("\nEncrypted message is: \n"+enc1)
dec = decipher(decipher(enc, key),key)
dec1 = dec.replace("0", "")
print("\nDecrypted message is: \n"+dec1)
