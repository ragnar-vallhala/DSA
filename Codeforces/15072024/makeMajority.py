   
       
def solve():
    k = input()
    s = input()
    
    i=0
    last=-1
    one=0
    zero=0
    
    while i<len(s):
        if last!=-1 and s[i]=='1':
            s = s[:last+1] + s[i:]
            last+=2
            one+=1
            zero+=1
            
        elif last==-1 and s[i]=='1':
            last+=1
            one+=1
        elif last==-1 and s[i]=='0':
            last=0          
        i+=1
    if last<len(s)-1:
        s = s[:last+3]
        zero+=1
    
    if one>zero:
        print("Yes")
    else:
        if s[0]=='1' and s[-1]=='1':
            print("Yes")
        else:
            print("No")
    



t = int(input())

for _ in range(t):
    solve()
