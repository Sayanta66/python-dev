# a = str(input("Enter the name of the first movie: "))
# b = str(input("Enter the name of the second movie: "))
# c = str(input("Enter the name of the third movie: "))
# movies = [a, b, c]
# print(movies)

a1 = int(input("Enter a number: "))
b1 = int(input("Enter a number: "))
c1 = int(input("Enter a number: "))
pal = [a1, b1, c1]
pal2 = [c1, b1, a1]
if(pal == pal2):
    print("This is a palindrome")
else:
    print("This is not a palindrome")