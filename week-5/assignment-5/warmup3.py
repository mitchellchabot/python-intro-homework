def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

names = ["Molly", "Mitchell", "Diana", "Poppy", "Kapri", "Borgenstein", "Gorbulax", "Goo", "Strawberry Goo"]
target = input("Enter a name to search for: ")
index = linear_search(names, target)

if index == -1:
  print(f"\"{target}\" was not found in the list.")
else:
  print(f"Found \"{target}\" at index {index}.")
