#a = list((1,2,'abc','xyz'))
#print(a)
#print(type(a))
#print(len(a))

#b = ['xyz','abc',123,44,55]
#print(a)
#print(type(a))
#print(len(a))

#a = ['robert','anuj','mishraji','saud','jadhav','nair']
#for i in a:
    #if i[-1]=='i':
      #print(i)



#a = ['robert','anuj','mishraji','saud','jadhav','nair']
#for i in a:
   #if 'r' in i:
    #  print(i)


a = ['robert','anuj','mishraji','saud','jadhav','nair']
for i in a:
   for j in i:
      if j=='r':
         print(i)
         break


#while loop

a = ['robert','anuj','mishraji','saud','jadhav','nair']
i = 0
while i<len(a):
   j=0
   c=0
   print(a[i])
   while j<len(a[i]):
      if a [i][j] in 'aeiou':
        c=c+1
      j+=1
   print(f"{a[i]} this name contain {c} vowels")
   i+=1 

a = ['robert','anuj','mishraji','saud','jadhav','nair']
for i  in a:
   c=0
   for j in i:
      if j in 'aeiou':
         c=c+1
   print(f"{i} this name contains{c} vowels")

for i in a:
   if len(i)==6:
      print(i)




a = ['robert','anuj','mishraji','saud','jadhav','nair']
for i  in a:
   c=""
   for j in i.lower():
      if j in 'aeiou':
         c=c+j
   print(f"{i} this name contains {len(c)} ({c})vowels")



