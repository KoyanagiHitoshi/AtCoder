w,h,n=map(int,input().split())
b=c=0
for _ in [0]*n:
    x,y,a=map(int,input().split())
    if a==1:b=max(b,x)
    if a==2:w=min(w,x)
    if a==3:c=max(c,y)
    if a==4:h=min(h,y)
print([(w-b)*(h-c),0][(w<b)|(h<c)])