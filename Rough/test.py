def chr2int(s:str)->int:
    if len(s)!=1:
        raise "Invalid string!"

    for i in range(0x10ffff):
        if chr(i) == s[0]:
            return i
    raise "Invalid string!"

class Node:
    def __init__(self, value, key, next=None):
        self.key=key
        self.value=value
        self.next = None


class HashMap:
    def __init__(self,size=128):
        self.keys = []
        self.size = size
        self.table = [None]*size

    def insert(self,key:str,value:any)->None:
        index=hash(key)%self.size 
        if key in self.keys:
            root = self.table[index]
            while root!=None:
                if root.key==key:
                    root.value=value
                    return
                root = root.next
        else:
            self.table[index] = Node(value,key)
            self.keys.append(key)
    
    def get(self,key)->any:
        if key in self.keys:
            index = hash(key)%self.size 
            root = self.table[index]
            while root!=None:
                if root.key==key:
                    return root.value
                root = root.next
        else:
            return None
            
    def __str__(self)->str:
        result='{'
        for i in self.keys:
            result+=str(i)+':'+str(self.get(i))+', '
        result=result[:-2]+'}'
        return result

v = HashMap(1024)
import random
import time
t = time.time()
trials = 1e4
print(trials)
for i in range(int(trials)):
    ins = random.randint(0,0x10ffff)
    ser = random.randint(0,0x10ffff)
    v.insert(chr(ins),255)        
    a = v.get(chr(ins))
    if i%100:
        print(i,end="\r")
print(time.time()-t)

v={}
t = time.time()
for i in range(int(trials)):
    ins = random.randint(0,0x10ffff)
    ser = random.randint(0,0x10ffff)
    v[chr(ins)] = 255 
    try:          
        a = v[chr(ser)]
    except:
        pass
    if i%100:
        print(i,end="\r")
print(time.time()-t)
            
                    
                        
            