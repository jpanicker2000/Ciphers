def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
    
def flatten(t):
    return [item for sublist in t for item in sublist]

def keycipher(text1,text2,sel):
 text1 = text1.upper()
 vlist= []
 for char in text1:
    if char not in vlist:
        vlist.append(char)
 
 n = len(vlist)
 klist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
          'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
 templ = []
 for letter in klist:
    if letter not in vlist:
        templ.append(letter)
        
 
 vlist.extend(templ)
 newcipher=[]
 temp2 = []
 temp3 = []

 v3 = chunks(vlist,n)
 print("Intial")
 print(v3)
 for x in v3:
   if (len(x)<n):
      for v in x:
          temp2.append(v)
      print("temp2")
      print(temp2)
      v3.remove(x)
      print("v3 after removal")
      print(v3)
 for i in range(0,n):
    for x in v3:
        temp3.append(x[i])
 print("temp3")
 print(temp3)
 v3 = chunks(temp3, n)
 print("chunked v3")
 print(v3)    
 for l in v3:
     v3[v3.index(l)].append(temp2[v3.index(l)])
 print(v3)
 v3.sort(key=lambda b: b[0])
 v3 = flatten(v3)
 newcipher = v3 
 print(newcipher)
             
 


 cipher_dict = dict(zip(klist, newcipher))
 
 if sel == 0:    
     enc =""
     text2 = text2.upper()
     for i in text2:
        if i == " ":
            enc+= " "
        else:
            enc+=cipher_dict[i]
     print(cipher_dict)    
     return enc
 elif sel ==1:
     dec =""
     text2 = text2.upper()
     for i in text2:
        if i == " ":
            dec+= " "
        else:
            dec+=klist[newcipher.index(i)]
          
     return dec
 else:
     print("Please enter 0 for encryption or 1 for decryption")

key="electronics"
s = "Actions Speak Louder Than Words"
print("Plaintext: "+s)
print("Key: "+key+"\n")


# Keyword Transposed Cipher
print("Keyword Transposed Cipher -\n")
c1 = keycipher(key,s,0)
c2 = keycipher(key,c1,1)
print("Encrypted text: "+c1)
print("Decrypted text:"+c2)
