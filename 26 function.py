####### Modules and package
#######module is a file containing python definition function and variable
#######it is collection of function and classes
#######types of modules
#######1) Built in module
#######2)User defind module
######
#######before using builtiing and user defined module python file we need to
#######inprot that madule in the python file
######
#######syntax
###import module_name
#######accessing a function inside module
#######module_name.fun_name()
######
########import math as m
########print(m.sqrt(4))
########print(m.factorial(5))
########print(m.pow(2,3))
########print(m.floor(15.9)) #round down number
########print(m.cell(15.2)) #round up number
########
########print(m.floor(-15.9))
########print(m.ceil(-15.2))
######import random as r
########print(r.random()) #====>[0,10)
########print(r.randrange(1,4)) #[a,b)
########print(r.randrange(1,4,6)) #[a,b)
######
######print(r.randrange(2,8,2)) #[a,b)
######print(r.randrange(20)) #[a,b)
######print(r.randrange(2)) #[a,b)
######print(r.randrange(2,6)) #[a,b)
######print(r.randrange(6,2)) #[a,b) error print
######
####s='python_programming'
####print(s[-15:-16])
####print(s[2:3:-1])
####
###print(r.randint(2,5))
###print(r.randit(6,2))
####
##print(r.uniform(2,5))
##
##
import random
l=['karan_arjun','big_boss','sholey']
random.shuffle(l)
print(l)
