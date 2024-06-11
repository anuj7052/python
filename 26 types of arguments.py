# types of Arguments
# 1) Positional Argument
# 2) Default Argument
# 3) Keyword Argument
# 4) Variable length Argument

### 1) Positional Argument -- During a function call, values passed through
##  arguments should be in the order of parameters in the function definition.
##  This is called positional arguments.
##  ♫Keyword arguments should follow positional arguments only
def simple_int(p,r,t):
    print('Principle is:',p)
    print('rate is:',r)
    print('time is:', t)

    si=p*r*t/100
    print('simple intrest is:', si)




p=5000
r=10
t=5
simple_int(p,r,t)


### 2) Default Argument Default values indicate that the function argument will take that
##     value if no argument value is passed during the function call.

def simple_int(p,r =10,t=8):
    print('Principle is:',p)
    print('rate is:',r)
    print('time is:', t)

    si=p*r*t/100
    print('simple intrest is:', si)




p=5000
r=10
t=5
simple_int(p)

def simple_int():
    print('Principle is:',p)
    print('rate is:',r)
    print('time is:', t)

    si=p*r*t/100
    print('simple intrest is:', si)




p=5000
r=10
t=5
simple_int()


def simple_int(p,r,t=5.5):
    print('Principle is:',p)
    print('rate is:',r)
    print('time is:', t)

    si=p*r*t/100
    print('simple intrest is:', si)




p=5000
r=10
t=5
simple_int(p,r)


# 3) Keyword Argument Keyword Arguments - Python allows to pass function
#arguments in the form of keywords which are also called named arguments.


def simple_int(r,t,p):
    print('Principle is:',p)
    print('rate is:',r)
    print('time is:', t)

    si=p*r*t/100
    print('simple intrest is:', si)


simple_int(p=400,r=12,t=10)

