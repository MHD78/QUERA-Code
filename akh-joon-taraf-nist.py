
m=''
for i in range(3):
    q=int(input())
    n=input()
    m=m+n+' '
m=m.split(' ')
m=m[:-1]
shanbe=0
yekshanbe=0
doshanbe=0
seshanbe=0
charshanbe=0
pangshanbe=0
jome=0
for i in m:
    if i=='shanbe':
        shanbe += 1
    if i=='1shanbe':
        yekshanbe += 1
    if i=='2shanbe':
        doshanbe += 1
    if i=='3shanbe':
        seshanbe += 1
    if i=='4shanbe':
        charshanbe += 1
    if i=='5shanbe':
        pangshanbe += 1
    if i=='jome':
        jome += 1
        
datelist=[shanbe,yekshanbe,doshanbe,seshanbe,charshanbe,pangshanbe,jome]
z=0
for i in datelist:
    if i==0:
        z=z+1
print(z)
   