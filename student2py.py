l1=[]
n=int(input("enter the number of students:"))
for i in range(1,n+1):
    name=input("enter student name:")
    marks1=int(input("enter marks in physics:"))
    marks2=int(input("enter marks in chemistry:"))
    marks3=int(input("enter marks in maths:"))
    total=marks1+marks2+marks3
    average=total/3

print("----------STUDENT MARKSHEET----------")
print("__________________________")
print("name\tmarks\tmarks2\tmarks3\ttotal\taverage")
for i in range(len(l1)):
    l1.append(name)
    l1.append(marks1)
    l1.append(marks2)
    l1.append(marks3)
    l1.append(total)
    l1.append(average)  
print(l1)    