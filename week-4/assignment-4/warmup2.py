student = {"name": "Mitchell", "grade": "1st", "subjects":["Math", "Science", "History"]}
for key, value in student.items():
  print(f"{key}: {value}")
student["graduated"] = False
print(student)