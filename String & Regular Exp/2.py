#Check that the entire string starts with âfâ, ends with âoâ
#and contain one letter in between

import re
if re.match("f..o$","ftto sachin"):
    print("Matched")
else:
    print("Not matched")
