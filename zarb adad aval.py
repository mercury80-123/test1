n=int(input())

m=0
i=0
num=0

while 1001<n<=2:
    for m in range(1,n+1):
        if n%m==0:
            for i in range(2,1001):
                num=0
                for d in range(1,i+1):
                    if m%d==0:
                        num+=1
                    if num==2:
                        i*=i
                        i=m
print(i)
