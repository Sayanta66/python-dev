n = int(input("Enter a number: "))
if(n==999):
    print("This is the greatest number")
elif(100<n<999):
    print("This is a normal three digit number")
else:
    print("This is not a valid entry")

a = int(input())
b = int(input())
c = int(input())
if(a>b and a>c):
    print("a is the greatest")
elif(b>a and b>c):
    print("b is the greatest")
else:
    print("c is the greatest")

a = int(input("Enter a number: "))
if(a>7 and a%7==0):
    print("Multiple of 7")
elif(a>7 and a%7!=0):
    print("Not a multiple of 7")
else:
    print("Not a valid input")