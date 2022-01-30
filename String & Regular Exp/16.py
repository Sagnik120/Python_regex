import re
str = input()
array = re.findall('[0-3]+', str)
print(array)
