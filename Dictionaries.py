student_info = {
    "firstname" : "Sayanta",
    "lastname" : "Banerjee",
    "rollno." : 36,
    "subjects" : ["maths", "physics", "chemistry"],
    "Sections" : ("A", "B")
}
print(student_info)
print(type(student_info))
print(student_info["firstname"])

student_info["firstname"] = "Adita"
student_info["lastname"] = "Pal"
print(student_info)