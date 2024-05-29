a = (1,2,3,'abc','xyz')
print(a)
print(type(a))
print(len(a))
print(a[-1])

b = (1,2)
print(type(a+b))
s = (1,)
print(type(s))

data = ('anuj',555,'thane',11,222,333,44,55)
(name,age,city,*a) = data
print(city)
print(a)
print(a[2])

a=[1,2,3,([33,88,'bc'('yes','No','yes')])]
#a[3][3] = ('yes','yes','yes')

b = list(a[3][3])
b[1] = 'yes'
a[3][3] = tuple(b)
print(a)

a = (1,2,3,3,4,3)
print(a[: :-1])
print(a.count(2))