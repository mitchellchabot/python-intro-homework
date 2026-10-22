
number = int(0input("Enter a number: "))

if number < 0:
  print(f"{number} is a negative")
elif number == 0:
  print("0 is zero")
else:
  print(f"{number} is a positive")

if number % 2 == 0:
  print(f"{number} is even")
else:
  print(f"{number} is odd")