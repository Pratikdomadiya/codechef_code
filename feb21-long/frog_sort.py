# cook your dish here
t=int(input())
while(t!=0):
    n=int(input())
    w=list(map(int,input().split()))
    l=list(map(int,input().split()))
    index_dict={}
    l_dict={}
    sort_w=sorted(w)
    for i in range(len(w)):
        index_dict[w[i]]=i
        l_dict[w[i]]=l[i]
    jump=0
    for i in range(1,len(sort_w)):
        ind1=index_dict[sort_w[i-1]]
        ind2=index_dict[sort_w[i]]

        while(ind1>=ind2):
            ind2=ind2+l_dict[sort_w[i]]
            index_dict[sort_w[i]]=ind2
            jump+=1
            
    print(jump)
    t-=1