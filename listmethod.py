a = [1,2,3,'hkjhds','kjhlfgkj']
a.append("Added")
print(a)

a = [1,2]
b = [3,4]
a.extend(b)
b.extend(a)
print(b)

a = [1,2,3,4]
a.insert(0,100)
a.insert(0,100)
print(a)

a = ['abc',100,200]
a[1] = 'anuj'
print(a)

a = [1,2,3,4,4,5]
a.pop()
a.remove(1)
print(a)

a = [1,2,3,4,4,5]
del()
print(a)

ab = [1,2,3,4,4,5,6]
print(ab.count(4))
ab.reverse()
print (ab)