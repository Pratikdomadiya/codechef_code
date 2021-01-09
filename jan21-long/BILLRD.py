T=int(input())
while(T!=0):
    N,K,x,y=map(int,input().split())
    if x==y:
        print(N,N)
    else:
        temp=[]
        side_no=int((K-1)%4)
        if x>y:
            temp=[[N,y+N-x],[y+N-x,N],[0,x-y],[x-y,0]]
        if x<y:
            temp=[[x+N-y,N],[N,x+N-y],[y-x,0],[0,y-x]]
        final_cord=temp[side_no]
        print(final_cord[0],final_cord[1])   
    T=T-1
