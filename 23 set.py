a = {'aa','xyz','ppq'}
a.add('rohit')
a.update({'rahul','roshan'})
print(a)
a.pop()
print(a)

for i in a:
    print(i)

#otp gentrate
a = {'1','2','3','4','5','6','7','8','9','0'}
c =""
for i in a:
    c = c+i

print(c[0:4:1])
