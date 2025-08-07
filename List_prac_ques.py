# a = str(input("Enter the name of the first movie: "))
# b = str(input("Enter the name of the second movie: "))
# c = str(input("Enter the name of the third movie: "))
# movies = [a, b, c]
# print(movies)

# a1 = int(input("Enter a number: "))
# b1 = int(input("Enter a number: "))
# c1 = int(input("Enter a number: "))
# pal = [a1, b1, c1]
# pal2 = [c1, b1, a1]
# if(pal == pal2):
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")

a1 = int(input("Enter a number: "))
b1 = str(input("Enter a string: "))
c1 = str(input("Enter another string: "))
d1 = int(input("Enter a number: "))
pal = [a1, b1, c1, d1]
pal1 = pal.copy()
pal2 = pal1[::-1]
print(pal1, pal2)
if(pal == pal2):
    print("This is a palindrome")
else:
    print("This is not a palindrome")