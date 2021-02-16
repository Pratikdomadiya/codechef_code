t=int(input())
while(t!=0):
    n=int(input())
    l=list(map(str,input().split()))
    list_l={}
    for i in l:
        st=i[1:]
        if st in list_l:
            list_l[st].append(i[0])
        else:
            list_l[st]=[i[0]]
    keys=list(list_l.keys())
    c=0
    # print(len(body))
    for i in range(len(list_l)):
        for j in range(i+1,len(list_l)):
            t1=list_l[keys[i]]
            t2=list_l[keys[j]]
            temp=len(set(t1).intersection(t2))
            c=c+((len(t1)-(temp))*(len(t2)-(temp)))*2
    print(c)
    t-=1