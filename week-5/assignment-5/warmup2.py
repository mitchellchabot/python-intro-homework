while True:
  num = input("Enter a positive integer: ")
  try:
    if int(num) < 0:
      # num is a negative int
      print("That's not a positive integer. Try again")
    else:
      print(f"Got it: {int(num)}")
      break;
  except:
    # error was thrown!
    # num is not a number
    print("That's not a positive integer. Try again")
