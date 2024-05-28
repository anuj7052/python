#evennumber and prime number diffrent-diffrent list
a = [1,2,3,4,5,6,7,8,9,10]
e = []
o = []
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)

#duplicate value
#a = [1,2,3,4,5,6,7,7,6]
c=0
for i in range(0,len(a),1):
    c1 = 0
    for j in range(i+1,len(a),1):
        if a[i] == a[j]:
            c1 = c1+1
            c = c+1
            print(f"duplicate number are{a[i]} ={c1}")
print(f"total duplicate {c}")

a = [1,2,3,4,5,6,7,7,6,6]
b = []
c1=[]

for i in a:
    if i not in b:
        b.append(i)
    else:
        c1.append(i)
print(b)
print(c1)
for i in b:
    c2 = 0
    for j in c1:
        if j == i:
            c2 = c2+1
    if c2:
        print(f"{i} duplicate are {c2}")



#a=[[['robert','mishraji','anuj','rajit','jadhav']]]
#for i in a[0][0]:
#    print(i)

b = [[1,2,3,4],[5,6,7,8,9],[9,10,11,12]]
for i in b:
    for j in i:
        print(j)


b = [[1,2,3,4],[5,6,7,8,9],[9,10,11,12]]
row = 1
while row<=len(b):
    col+=1
    

