import re

string = "Python is fun Python"

# check if 'Python' is at the beginning
match = re.match('Python', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

