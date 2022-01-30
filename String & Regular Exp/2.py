#Check that the entire string starts with ‘f’, ends with ‘o’
#and contain one letter in between

import re
if re.match("f..o$","ftto sachin"):
    print("Matched")
else:
    print("Not matched")
