##variation in user defined function
##
##function with no argument no return value
##function with argument no return value
##function with no argument but return value
##function with argument and return value

##def add():
##    a=10
##    b=20
##    print(f'addittion of {a}and {b} is:',a+b)
##add()
##
##def add(a,b):
##    print(f'addittion of {a}and {b} is:',a+b)
##a=10
##b=20
##add(a,b)

def add(a,b):
    a=10
    b=20
    return a+b
    #return f'addittion of {a}and {b} is:',a+b
    print('hii') # after  return no excutable
sum=add()
print(sum)
