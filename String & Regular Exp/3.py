#Check that the entire string starts with ‘f’, ends with ‘o’
#and contain two letter in between

import re
if re.match("f..o$","fooo"):
    print("Matched")
else:
    print("Not matched")
