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

null_dict = {}
print(null_dict)

player = {
    "Firstname" : "Lionel",
    "Lastname" : "Messi",
    "Stats" : {
        "Attack" : 95,
        "Defence" : 75,
        "Goals Per Game" : 2.5 
    }   
}
print(player)
print(player["Stats"])
print(player["Stats"]["Attack"])
print(player.keys())
print(player["Stats"].keys())

print(list(player.keys()))
print(list(player["Stats"].keys()))
print(len(list(player.keys())))
print(len(player.keys()))

employee = {
    "Firstname" : "Sayanta",
    "Lastname" : "Banerjee",
    "Company" : "Keysight Technologies",
    "Years of experience" : 4.2,
    "Skills" : {
        "Core" : "Documentation",
        "Secondary" : "DevOps",
        "Tertiary" : "Development"
    }
}
print(employee.values())
print(employee.items())
print(employee["Skills"].items())
print(list(employee.values()))
print(list(employee.items()))

employee1 = list(employee.items())
print(employee1[0])