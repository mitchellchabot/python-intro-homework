while True:
  numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
  print("=== Number Cruncher ===")
  print("1. Find minimum")
  print("2. Find maximum")
  print("3. Search for a number")
  print("4. Sort the list")
  print("5. Quit")
  option = input("Choose an option (1-5): ")
  if option == "1":
    minimum = numbers[0]
    for num in numbers:
      if num < minimum:
        minimum = num
    print(minimum)
  elif option == "2":
    maximum = numbers[0]
    for num in numbers:
      if num > maximum:
        maximum = num
    print(maximum)
  elif option == "3":
    num = input("Please enter a number to search for: ")
    found = False
    for i in range(len(numbers)):
      if numbers[i] == int(num):
          found = True
          print(f"Found at index {i}.")
    if not found:
       print("Not found.")
  elif option == "4":
     while True:
        swapped = False
        for i in range(1, len(numbers)):
           left = numbers[i - 1]
           right = numbers[i]
           if left > right:
              numbers[i - 1] = right
              numbers[i] = left
              swapped = True
        if swapped == False:
          break
     print(numbers)
  elif option == "5":
     print("Goodbye (Quitters never prosper...)")
     break
  else:
    print("Please enter a valid option next time.")