#Including a ‘$’ at the end will match only strings of length 2
import re
if re.search("..$","fooo gh"):
    print("Matched")
else:
    print("Not matched")
