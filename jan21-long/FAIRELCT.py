# cook your dish here
T=int(input())
for test in range(T):
    N,M=input().split()
    N=int(N)
    M=int(M)
    N_elem=list(map(int,input().split()))
    M_elem=list(map(int,input().split()))
    count=0
    sum_N=int(sum(N_elem))
    sum_M=int(sum(M_elem))
    max_M=0
    min_N=0
    N_elem=sorted(N_elem)
    M_elem=sorted(M_elem,reverse=True)
    while sum_N<=sum_M and count<min(len(N_elem),len(M_elem)):
        max_M=M_elem[count]
        min_N=N_elem[count]
        N_elem[count]=max_M
        M_elem[count]=min_N
        sum_N=sum_N-min_N+max_M
        sum_M=sum_M-max_M+min_N
        count=count+1
   
    if sum_N>sum_M:
        print(count)
    else:
        print('-1')