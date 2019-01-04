n,m=[int(x) for x in input().split()]

tomb=list()
for i in range(n):
    tomb.append([int(x) for x in input().split()])
    
i=0
while i<n and sum(tomb[i])>0:
    i+=1
if i<n:
    print(i+1)
else:
    print("0")
