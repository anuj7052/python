a = {'name':'ABC',0:'kuch bhi','age':78,'name':'jfdslkhf'}
print(a)
print(len(a))
print(type(a))

a['age'] = 20
a['city'] = 'thane'
# a['name']= 'Anuj'
print(a)

for i in a:
    print(f"{i} = {a[i]}")


print(a.keys())
print(a.values())
print(a.items())

for k,v in a.items():
    print(k,v)
