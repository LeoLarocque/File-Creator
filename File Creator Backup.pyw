#Go to HugoLarocque777, (he's my little brother) if you want to see some more cool code!
import time
def function():
  if name == "Leo":
      print("Hello " + name + ", creater of this program. It's nice to see you.")
  else:
      print("Hello " + name + ", it's nice to see you.")
  bDay = input("Enter you birth day. Month, Day, Year. ")
  bDayRep = bDay.replace(",", "")
  email = input("Enter email: ")
  name1 = name+".txt"
  f = open(name1, "w")
  f.write("Name: " + name + "\nBirth Date: " + bDayRep + "\nEmail: " + email)
  f.close()
name = input("Enter full name: ")
nameSplit = name.split()
while len(nameSplit) <= 2:
  name = input(name + " enter your full name including middle name. ")
  function()
  exit()
def function():
  if name == "Leo":
      print("Hello " + name + ", creater of this program. It's nice to see you.")
  else:
      print("Hello " + name + ", it's nice to see you.")
  bDay = input("Enter you birth day. Month, Day, Year. ")
  bDayRep = bDay.replace(",", "")
  email = input("Enter email: ")
  name1 = name+".txt"
  f = open(name1, "w")
  f.write("Name: " + name + "\nBirth Date: " + bDayRep + "\nEmail: " + email)
  f.close()
function()
