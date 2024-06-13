# types of Arguments
# 1) Positional Argument
# 2) Default Argument
# 3) Keyword Argument
# 4) Variable length Argument

### 1) Positional Argument -- During a function call, values passed through
##  arguments should be in the order of parameters in the function definition.
##  This is called positional arguments.
##  ♫Keyword arguments should follow positional arguments only
##def simple_int(p,r,t):
##    print('Principle is:',p)
##    print('rate is:',r)
##    print('time is:', t)
##
##    si=p*r*t/100
##    print('simple intrest is:', si)
##
##
##
##
##p=5000
##r=10
##t=5
##simple_int(p,r,t)


### 2) Default Argument Default values indicate that the function argument will take that
##     value if no argument value is passed during the function call.

##def simple_int(p,r =10,t=8):
##    print('Principle is:',p)
##    print('rate is:',r)
##    print('time is:', t)
##
##    si=p*r*t/100
##    print('simple intrest is:', si)




##p=5000
##r=10
##t=5
##simple_int(p)

##def simple_int():
##    print('Principle is:',p)
##    print('rate is:',r)
##    print('time is:', t)
##
##    si=p*r*t/100
##    print('simple intrest is:', si)
##
##
##
##
##p=5000
##r=10
##t=5
##simple_int()
##
##
##def simple_int(p,r,t=5.5):
##    print('Principle is:',p)
##    print('rate is:',r)
##    print('time is:', t)
##
##    si=p*r*t/100
##    print('simple intrest is:', si)
##
##
##
##
##p=5000
##r=10
##t=5
##simple_int(p,r)


# 3) Keyword Argument Keyword Arguments - Python allows to pass function
#arguments in the form of keywords which are also called named arguments.


##def simple_int(r,t,p):
##    print('Principle is:',p)
##    print('rate is:',r)
##    print('time is:', t)
##
##    si=p*r*t/100
##    print('simple intrest is:', si)
##
##
##simple_int(p=400,r=12,t=10)
##


# scope: scope is part of program in which variable can be usead.
#1) Local scope
#2) Global Scope

#1) A variable can be decleared inside the function is  called  asa local scope

#scope of local variable is inside the function only
##def display():
##    a=10
##    print(a)
##print(a)
##display()

# global v==> A variable can decleared outside of function is called to gloabal scope
# scope of gloBAL variable is inside as well as outside the function

##A=15
##def display():
##    a=10
##    b=30
##    print(a)
##    print(A)
##print(A)
##display()
##print(A)


# whAT if?  A variable is decleared inside as well as outsde

##A=30
##def display ():
##    A=20
##    print(A)
##print(A)
##display()
##print(A)
##
##
##A=30
##def display ():
##    global A
##    A=20
##    print(A)
##print(A)
##display()
##print(A)

##B=30
##def display(x):
##    global a
##    a=a+x
##    return a
##a=20
##b=5
##display(b)
##print(a)

##a=10
##y=5
##def myfun():
##    a=2
##    y=a
##    print(y,a)
##myfun()
##print(y,a)
##
##a=10
##y=5
##def myfun():
##    y=a
##    a=2
##    print(y,a)
##myfun()
##print(y,a)

a=10
y=5
def myfun():
    global a
    y=a
    a=2
    print(y,a)
myfun()
print(y,a)

a=10
y=5
def myfun():
    global a
    a=2
    y=2
    print(y,a)
myfun()
print(y,a)

a=1
def display():
    return a
print(a)
print(display())
print(a)



























