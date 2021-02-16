# cook your dish here
def minutes_converter(time,spell):
    t=time.split(':')
    hr=int(t[0])
    minutes=int(t[1])
    total_minutes=0
    if hr==12:
        if spell=='AM':
            total_minutes=minutes
        else:
            total_minutes=(minutes)+12*60
    else:
        if spell=='AM':
            total_minutes=hr*60+minutes
        else:
            total_minutes=(hr*60+minutes)+12*60
    return total_minutes  
        
# print(minutes_converter('12:00','AM')) 
t=int(input())
while(t!=0):
    p=input().split()
    sum_p=minutes_converter(p[0],p[1])
    n=int(input())
    ans=''
    while n!=0:
        f_time=input().split()
        if minutes_converter(f_time[0],f_time[1])<=sum_p<=minutes_converter(f_time[2],f_time[3]):
            ans=ans+'1'
        else:
            ans=ans+'0'
        n-=1
    if ans=='':
        print('-1')
    else:
        print(ans)   
    t-=1
    