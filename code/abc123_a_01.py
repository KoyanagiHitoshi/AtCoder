a,b,c,d,e,k=[int(input()) for i in range(6)]
print("Yay!" if abs(a-b)<=k and abs(a-c)<=k and abs(a-d)<=k and abs(a-e)<=k and abs(b-c)<=k and abs(b-d)<=k and abs(b-e)<=k and abs(c-d)<=k and abs(c-e)<=k and abs(d-e) else ":(")