a,b,n=(int(input()) for _ in range(3))
while n%a+n%b:n+=1
print(n)