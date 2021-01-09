t=int(input())
while(t--!=0):
    n=int(input())
    m=list(map(int,input().split()))
    pos_count=0
    neg_count=0
    for i in m:
        if i>0:
            pos_count+=1
        if i<0:
            neg_count+=1
    print(neg_count*pos_count)