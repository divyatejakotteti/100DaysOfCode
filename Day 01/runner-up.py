n=int(input())
l=list(set(map(int,input().strip().split())))
l.sort()
print(l[-2])
