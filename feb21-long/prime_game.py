# cook your dish here
def SieveOfEratosthenes(n, primeCount):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True): 
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    count = 0
    
    for p in range(2, n+1):
        if prime[p]:
            count+=1
        primeCount[p] = count 
        
t=int(input())
primeCount = [0]*1000001
SieveOfEratosthenes(1000000, primeCount)
while(t!=0):
    x,y=map(int,input().split())
    n=0
    if y==1:
        if x>2:
            print("Divyam")
        else:
            print("Chef")
    else:
        n = primeCount[x]
        print("n: "+str(n))
#         for i in range(2,x+1):
#             if (i%2==0 and i!=2) or (i%3==0 and i!=3) or (i%5==0 and i!=5 ) or (i%7==0 and  i!=7) :
#                 continue
#             else:
#                 n+=1
#                 if n>y:
#                     break
#                 # print(i)
        if n<=y:
            print("Chef")
        else:
            print("Divyam")
    t-=1