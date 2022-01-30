import re

pattern = 's....n$'
test_string = 'sachin'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
