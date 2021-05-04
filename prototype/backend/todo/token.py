import time

def change(x, y):
    sto = ''
    for chara in range(len(x)):
        position = chara + y
        if position > len(x) - 1:
            position = position - len(x)
        sto += x[position]
    return sto

def enctry(s):
    k = '&^*ghjsdgsewtqgfdhsdsdagsaGF43^&*%87jfhgdsafasg'
    ticks = time.time()
    k = change(k,(int(((ticks - 10000) / 86400 ) % 30)))
    
    
    encry_str = ""
    for i in range(len(s)):
        if i < len(s) - 1:
            temp = str(ord(s[i])+ord(k[i]))+'_' 
        else:
            temp = str(ord(s[i])+ord(k[i]))
        
        encry_str = encry_str + temp
    
    return encry_str
 

def dectry(p):
    k = '&^*ghjsdgsewtqgfdhsdsdagsaGF43^&*%87jfhgdsafasg'
    ticks = time.time()
    k = change(k,int(((ticks - 10000) / 86400 ) % 30))
    dec_str = ""
    p = p.split("_")
    for i in range(len(p)):
        temp = chr(int(p[i]) - ord(k[i])) 
        dec_str = dec_str + temp
    return dec_str
 
