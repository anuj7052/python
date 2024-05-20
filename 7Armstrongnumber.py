n=8208
nl = n
l = len(str(n))
s=0
while n!=0:
    r= n%10
    s = s+r**l
    n = n//10
if nl == s:
    print("This is an Armstrong Number")
else:
    print("Not A Armsyrong NUmber")

 
