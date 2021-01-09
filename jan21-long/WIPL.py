T=int(input())
while(T!=0):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    h1=[]
    sum_h=0
    h=sorted(h)
    h1.append(h[n-1])
    sum_h=h[n-1]
    z=-1
    for i in range(n-2,-1,-1):
        h2=[]
        sum_h+=h[i]
        for i1 in h1:
            p=i1
            h2.append(p)
            h2.append(h[i])
            h2.append(p+h[i])
#             print(p)
#             print(h[i])
#             print(sum_h)
#             print(k)
            if(((p+h[i])>=k)and((sum_h-p-h[i])>=k)):
                z=n-i
                break
            if(((h[i])>=k)and((sum_h-h[i])>=k)):
                z=n-i
                break
    
        if(z!=-1):
            break
        h1=h2
    print(z)
      
    T=T-1
