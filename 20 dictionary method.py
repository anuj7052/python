a = {'name':'abc','age':55,'city':'thane'}
print(a['name'])
print(a.get('name'))
print(a.get('age'))

a['phone'] = 453434546
a.update({'tel':7676544687})

a.pop('name')
a.popitem()
# a.clear()
del a['age']
print(a)
