n=12
for i in range(2,n,1):
    if n%i==0:
        print(n,"is not a prime number")
        break
    else:
        print(n,"Is an prime number")