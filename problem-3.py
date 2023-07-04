lis=[]
n=5
m=1
for i in range(n):
    lis.append(m)
    m=m+2
if (n%2==0):
    (lis.pop())
print(lis)