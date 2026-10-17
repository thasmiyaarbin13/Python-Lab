l2=['red',10,'green',20,'blue']
print(l2)
l2.append(30)
print(l2)
l2.insert(6,'black')
print(l2)
l2.extend([40,'lavender',60])
print(l2)
mixed_one=[]
mixed_two=[]
for item in l2:
    if isinstance(item,(int,float)):
        mixed_one.append(item)
    else:
        mixed_two.append(item)
print('mixed one=',mixed_one)
print('mixed_two=',mixed_two)
         