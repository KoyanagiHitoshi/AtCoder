N=int(input())
flag=False
for i in range(1,10):
    m=N/i
    if m==int(m) and 1<=m<=9:
        flag=True
        break
print("Yes" if flag else "No")