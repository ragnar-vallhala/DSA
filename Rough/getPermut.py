a='abbc'
b='cbabadcbbabbcbabaabccbabc'
d={}
for k in a:
    if k in d.keys():
        d[k]+=1
    else:
        d[k]=1
        
for i in range(len(b)-len(a)+1):
    dk={}
    for k in b[i:i+len(a)]:
        if k in d.keys():
            if k in dk.keys():
                dk[k]+=1
            else:
                dk[k]=1
        else:
            break
    f=0
    for k in d.keys():
        if k not in dk.keys() or dk[k]!=d[k]:          
            f=1
    if f==0:
        print(i,  b[i:i+len(a)])