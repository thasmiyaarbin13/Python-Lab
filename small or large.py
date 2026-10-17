a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if a>=b and a>=c:
    print(a,"is the largest number")
elif b>=c and b>=a:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")