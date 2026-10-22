day = input("What day of the week is it? (Monday - Sunday) ").title();
time = input("What time of the day is it? (Morning, Afternoon or Night) ").title();



if day != "Monday" and day!="Tuesday" and day !="Wednesday" and day !="Thursday" and day != "Friday" and day != "Saturday" and day !="Sunday":
  print("Please enter a valid day of the week")
if time != "Morning" and time != "Afternoon" and time != "Night":
  print("Please enter a valid time of day")

if (day == "Saturday"or day == "Sunday") and time == "Morning":
  print("Yoga is a great weekend Morning activity!")
elif (day == "Saturday" or day == "Sunday") and time == "Afternoon":
  print("An afternoon walk is a nice weekend afternoon activity!")
elif (day == "Saturday" or day == "Sunday") and time == "Night":
  print("Reading a good book is a relaxing weekend night activity! ")

if (day == "Monday" or day =="Tuesday" or day == "Wednesday") and time == "Morning":
  print("Meditating is a good start to a weekday morning!")
if (day == "Monday" or day =="Tuesday" or day == "Wednesday") and time == "Afternoon":
  print("Going for an afternoon walk is a good way to breakup the day")
if (day == "Monday" or day =="Tuesday" or day == "Wednesday") and time == "Night":
  print("Drinking some tea is a good way to relax before bed")

if (day == "Thursday" or day == "Friday") and time == "Morning":
  print("A pilates class is a good way to start the day")
if (day == "Thursday" or day == "Friday") and time == "Afternoon":
  print("Going to a cafe for lunch is a good way to breakup the day")
if (day == "Thursday" or day == "Friday") and time == "Night":
  print("Watching a good show is a nice way to relax")







