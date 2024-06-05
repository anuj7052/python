def Data():
    a = 1+2
    return a
print (Data())

#positional argument function
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"
print(data('rohit',21,'thane'))

# key word argument function
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(age=45,city='thane',name='abc'))