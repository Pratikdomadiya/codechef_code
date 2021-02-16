# cook your dish here
n=int(input())
if n>=2:
    for i in range(10,0,-1):
        if int(n%i)==0:
            print(i)
            break
else:
    print('-1')