marks = int(input("Enter obtained marks: "))
if(marks >= 50):
    print("Candidate Passed")
elif(40<marks<50):
    print("Candidate passed with Grace")
else:
    print("Candidate Failed")

n = int(input("Enter marks: "))
if(n%2!=0 and 50<n<80):
    print("Lucky Marks")
elif(n%2==0 and n>=80):
    print("Super Marks")
else:
    print("Unlucky Marks")