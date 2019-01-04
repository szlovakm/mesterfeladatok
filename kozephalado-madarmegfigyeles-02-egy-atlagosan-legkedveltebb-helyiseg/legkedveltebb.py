n,m=[int(x) for x in input().split()]

tomb=list()
for i in range(n):
    tomb.append([int(x) for x in input().split()])
    
m=0
s=0
for i in range(n):
    a=sum(tomb[i])
    if a>m:
        m=a
        s=i
print(s+1)
