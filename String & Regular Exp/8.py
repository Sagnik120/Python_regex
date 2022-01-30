#Check validity of Mobile Number (Shorter Code)

import re
number = input()
if re.match('^[789]{1}[0-9]{9}$',number):
    print('valid')
else:
    print('invalid')
