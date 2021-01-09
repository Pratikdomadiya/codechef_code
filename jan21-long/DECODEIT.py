# cook your dish here
st="abcdefghijklmnop"
T=input()
T=int(T)

for case in range(T):
    N=int(input())
    char=int(N/4)
    S=input()
    final_out=''
    for c in range(char):
        S1=S[c*4:4*(c+1)]
        st1=''
        for i in range(len(S1)):
            if S1[i]=='0':
                if st1=='':
                    st1=st[0:int(len(st)//2)]
                else:
                    st1=st1[0:int(len(st1)//2)]
            else:
                if st1=='':
                    st1=st[int(len(st)//2):]
                else:
                    st1=st1[int(len(st1)//2):]


        
        final_out=final_out+st1
    print(final_out)
    
