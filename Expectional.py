##print('hii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except:
##    print('annn')
##print("hello")


##print('hii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except Exception as e:
##    print(e)
##print("hello")


##try:
##    print('thane')
##    print(2/0)
##    print(int('demo'))
##    print('dadar')
##except ZeroDivisionError as e:
##    print(e)
##except valueError as v:
##    print(v)
##except Excesption as e:
##    print(e)
##except:
##    print('exception handeled')


##class  InvalidAgeError(Exception):
##    pass
##print("thane")
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print('exception handeled')
##print('Mumbai')
##
##
##class InvalidAgeError(Exception):
##    def __str__ (self):
##        return"Invalid Age Error Detected"
##age=int(input('Enter your Age: '))
##if (age>=18):
##    print('You can vote')
##else:
##    try:
##        raise InvalidAgeError()
##    except InvalidAgeError as e:
##        print(e)


class A:
    def __init__ (self,name,age):
        print('python developer')
        print(name,age)
    def show (self):
        print('Hii')
        
class B(A):
    def __init__ (self,name,age):
        super().__init__('raj',32)
        print('java developer')
        print(name , age)
        
    def display(self):
        print('Hello')
        
b= B('rajesh',31)

























    


