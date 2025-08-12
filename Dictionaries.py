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