t=int(input())
while(t!=0):
    n=int(input())
    A=list(map(int,input().split()))
    A=sorted(A)
    A1=A[-1]
    A2=A[-2]
    A3=A[0]
    print(abs(A1-A2)+abs(A2-A3)+abs(A3-A1))
    
#     print(A)
    
    t-=1