#Check that the entire string starts with âfâ, ends with âoâ
#and contain two letter in between

import re
if re.match("f..o$","fooo"):
    print("Matched")
else:
    print("Not matched")
