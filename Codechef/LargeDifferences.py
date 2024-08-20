# cook your dish here
t = int(input())


for _ in range(t):
    n = int(input())
    X = list(map(int,input().split()))
    P = list(map(int,input().split()))
    
    for i in range(n):
        chance = 2
        if i==0:
            k=i
            while k<n-1 and (X[k+1]-X[k])<=P[k]:
                k+=1
            if k>=n-2:
                print("YES1",i)
                break
            
            k+=1
            while k<n-1 and (X[k+1]-X[k])<=P[k]:
                k+=1
            if k>=n-1:
                print("YES2",i)
                break
        elif i==n-1:
            k=i
            while k>0 and (X[k]-X[k-1])<=P[k]:
                k-=1
            if k<1:
                print("YES3",i)
                break
            
            k-=1
            while k>0 and (X[k]-X[k-1])<=P[k]:
                k-=1
            if k<1:
                print("YES4",i)
                break
        else:
            k=i
            done=False
            while k>0 and (X[k]-X[k-1])<=P[k]:
                k-=1
            if k<1:
                done=True
            k=i+1
            while k<n-1 and (X[k+1]-X[k])<=P[k]:
                k+=1
            if done and k>=n-1:
                print("YES5",i)
                break
            else:
                k=i
                done=False
                while k>0 and (X[k]-X[k-1])<=P[k]:
                    k-=1
                if k<1:
                    done=True
                k=n-1
                while k>0 and (X[k]-X[k-1])<=P[k]:
                    k-=1
                if done and k<=i:
                    print("YES5",i)
                    break
                else:
                    k=i
                    done=False
                    while k<n-1 and (X[k+1]-X[k])<=P[k]:
                        k+=1
                    if k>=n-1:
                        done=True
                    k=i+1
                    while k<n-1 and (X[k+1]-X[k])<=P[k]:
                        k+=1
                    if done and k>=n-1:
                        print("YES5",i)
                        break
                    else:
                        k=i
                        done=False
                        while k>0 and (X[k]-X[k-1])<=P[k]:
                            k-=1
                        if k<1:
                            done=True
                        k=n-1
                        while k>0 and (X[k]-X[k-1])<=P[k]:
                            k-=1
                        if done and k<=i:
                            print("YES5",i)
                            break
                            
