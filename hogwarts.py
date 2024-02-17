students = ["Hermione", "Harry", "Ron", "Draco"]

houses = ["Griffindor", "Griffindor", "Griffindor", "Slytherin"]

#for student , house in zip(students, houses):
    #print(f"{student} lives in {house}")
    
    

# residences = []

# for i in range(len(students)):
#     residences.append((students[i], houses[i]))
    
# for residence in residences:
#     print(residence)

# students = {"Hermione": "Griffindor",
#             "Harry" : "Griffindor",
#             "Ron" : "Griffindor",
#             "Draco" : "Slytherin"
#             }

# for key, value in students.items():
#     print(key, "=>", value)

# 

students = [
            {"name" : "Hermione", "house" : "Griffindor", "patronus": "Otter"},
            {"name" : "Harry", "house" : "Griffindor", "patronus": "Stag"},
            {"name" : "Ron", "house" : "Griffindor", "patronus": "Jack Russel terrier"},
            {"name" : "Hermione", "house" : "Slytherin", "patronus": None}
            ]

for student in students:
    print(student['name'], student['house'], student['patronus'], sep=", ")