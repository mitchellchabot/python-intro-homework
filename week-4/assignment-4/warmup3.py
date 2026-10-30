list_one = ["Java", "Python", "C++", "Java Script"]
list_two = ["C++", "Java Script", "React", "SQL"]
set_one = set(list_one)
set_two= set(list_two)
print(set_one.union(set_two))
print(set_one.intersection(set_two))
print(set_one.difference(set_two))