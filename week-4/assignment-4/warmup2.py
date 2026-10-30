student = {"name": "Mitchell", "Grade": "1st", "Subjects":["Math", "Science", "History"]}
for key, value in student.items():
  print(f"{key}: {value}")
student["graduated"] = "False"
print(student)