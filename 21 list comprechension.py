odd =[x for x in range(1,101,1)]
print(odd)

even =[x for x in range(1,101,2)]
print(even)

a = ['robert','anuj','abc']
print([i.upper() for i in a])
print([i for i in a if 'b' in i])

a = ['robert','anuj','krushna','rajit','saud','ashish','virendra']
import random
random_element = random.choice(a)
print("Random element from the list:", random.choice(a))