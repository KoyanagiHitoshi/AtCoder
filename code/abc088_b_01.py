input()
l=sorted([int(_) for _ in input().split()])[::-1]
print(sum(l[::2])-sum(l[1::2]))