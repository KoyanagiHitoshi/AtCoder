s=list(input())
n=len(s)
zero=s.count("0")
one=s.count("1")
if n==1:print(0)
else:print(2*min(zero,one))