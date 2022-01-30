import re

pattern ='ViT'


String1 ='Hello VIT, Vellore, No.1'
String2 ='VIT No.1 Private University in India'

# Use of re.search() Method
print(re.search(pattern, String1))

# Use of re.match() Method
print(re.match(pattern, String1, re.IGNORECASE))

print(re.match(pattern, String2, re.IGNORECASE))

# Use of re.search() Method
print(re.search(pattern, String2, re.IGNORECASE))


