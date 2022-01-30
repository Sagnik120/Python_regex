#It searches only for the pattern ‘f.o’ in the string

import re
if re.match("f...o","fyyuo"):
    print("Matched")
else:
    print("Not matched")


