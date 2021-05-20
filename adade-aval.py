import math
n=int(input())
x=0
for i in str(n):
	x=x+int(i)
def aval(n):
    k=0
    for i in range(1,n):
        if n%i == 0:
            k=k*10+i
    if int(math.log(k))+1==1:
        return True
    else: return False
    
z=0
t=0
for j in range(n+1,10**5):
    r=aval(j)
    if r==True:
            z=z+1
            t=j
    if z==x:
            break
print(t)
            