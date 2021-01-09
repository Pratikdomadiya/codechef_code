test=int(input())
for i in range (test):
    n,k,d=(input().split())
    n=int(n)
    k=int(k)
    d=int(d)
    s=0
    prob=input().split()
    prob = [ int(x) for x in prob ]
    s=int(sum(prob))
    print(s//k) if s//k<=d else print(d)# cook your dish here
