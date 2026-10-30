students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Find the top scorer — loop through the list and track
# the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
# creting an int for the highest score starting with the first score of 88 at position 0 in the list
high_score = students[0]["score"]
#creating an object for the highest scoring student
highest_student= ""
#creating for loop to go through the list of students
for student in students:
# comparing each scor to the previous high score
  if student["score"] > high_score:
# setting the newest high score as the high score value
    high_score = student["score"]
# assigning the highest score with the related student name
    highest_student = student["name"]
# printing the highest scoring student and highest score
print(f"Top scorer: {highest_student} ({high_score})")

# Calculate the class average
# — accumulate the total score in a loop, then divide
# setting the total as 0 before looping though the list
total = 0
# going through the list of students
for student in students:
# summing the students scores as the loop goes through the list
  total += student["score"]
# assining the average value as the total scores divided by the number of students
average = total / len(students)
# printing the average score of the class
print(f"Classe average: {average}")


# List all unique subjects — use a set to collect
# subjects as you loop, then print them.
# creating a new set to find the unique values
unique_subjects = set()
# looping through the list to find the unique values
for item in students:
# adding the values to the set
  unique_subjects.add(item["subject"]) # add to set
# print the unique subjects offered
print(f"Subjects Offered: {unique_subjects}")

# List high scorers — use a loop and .append() to get
# the names of all students who scored above 75.

# list of students who score above 75
high_scorers = []
# iterate through students
for student in students:
  # check if student has score above 75
  if student["score"] > 75:
    # append student nme to list
    high_scorers.append(student["name"]) # append to list
# print list of student names
print(f" High scorers: {high_scorers}")

test = set([1, 2])
test.add(3)
print(test) # {1, 2,3}
test.add(2)
print(test) #{1, 2, 3}
test.add(1)
print(test) # {1, 2, 3}
test.add(150)
print(test) # {1, 2, 3, 150}
test.add(2)
print(test) # {1, 2, 3, 150}

l = [1, 2]
l.append(3)
print(l) # [1, 2, 3]
l.append(2)
print(l) # [1, 2, 3, 2]
l.append(1)
print(l) # [1, 2, 3, 2, 1]
l.append(1)
print(l) # [1, 2, 3, 2, 1, 1]



