# oops =  Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects. 
a=10
print(type(a))

a="anuj"
print(type(a))

##class student:
##    name='anuj'
##    email='anujsingh705223@GMAIL.COM'
##    roll_no=121
##    def demo(s):
##        name='anuj'
##        print(name)
##    
##s= student()
####print(s.name)
####print(s.email)
####print(s.roll_no)
##s.demo()


##class student:
##    name='anuj'
##    email='anujsingh705223@GMAIL.COM'
##    roll_no=121
##    def demo(self): #self is  default paramter that represent instance of class
##        name='anuj'
##        print(name)
##    
##s= student()
##s.demo()
##k=student()
##k.demo()
##
##m=student()
##m.demo()


##class A:
##    def demo(self,department):
##        print(self)
##        name ='anuj'
##        age='21'
##        roll_no=123
##        print(name,age,roll_no)
##    def display (self):
##        email='anujsingh@gmail.com'
##        address='ghatkpper'
##        print(email,address)
##a=A()
####a.demo()
####print(a)
####a.display()
####A.demo('ab')
##
##a.demo('mech')


##class student:
##    def show (self,name,rollno):
##        print('my name is ',name)
##        print('RSoll no is',rollno)
##        print('I am a Python Developer')
##
##    def display(self):
##        print('java developer')
##
##s=student()
##s.show('Anuj',123)
##s.display()

class student:
    name='anuj'
    email='gmail.com'
    def show (self):
        print(self.name,self.email)
        print('python developer')
    def display(self):
        print(self.name)
        print('java developer')
a=student()
#print(a.name)
a.show()
a.display()
        









































