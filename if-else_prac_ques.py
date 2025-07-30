# n = int(input("Enter a number: "))
# if(n==999):
#     print("This is the greatest number")
# elif(100<n<999):
#     print("This is a normal three digit number")
# else:
#     print("This is not a valid entry")

a = int(input())
b = int(input())
c = int(input())
if(a>b and a>c):
    print("a is the greatest")
elif(b>a and b>c):
    print("b is the greatest")
else:
    print("c is the greatest")