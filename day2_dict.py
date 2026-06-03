

My_profile = {
    "Name" : "Anushree Kavaloor",
    "Skill" : "Python basics",
    "Goal" : "GenAI engineer by 2029",
    "Study_time" : 45,
    "Day" : 2
}
#Access and print
print("Name: ",My_profile["Name"])
print("Goal: ",My_profile["Goal"])

#Updating item
My_profile["Skill"] = "Python + dict"

#Adding a new item
My_profile["City"] = "Ballari"

#Print full dict
print("My full profile: ", My_profile)
