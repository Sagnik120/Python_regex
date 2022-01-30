#Check validity of PAN card number with RE

import re
pan=input()
if len(pan) < 10 or len(pan) > 10 :
    print ("PAN Number should be 10 characters")
    exit
elif re.search("[0-9]",pan[0:5]):
    print ("Invalid - 1")
    exit
elif re.match("[A-Za-z]",pan[5:9]):
    print ("Invalid - 2")
    exit
elif re.match("[0-9]",pan[-1]):  
    print ("Invalid - 3")
    exit
else:
    print ("Your card "+ pan + " is valid")


#AFNPV1234V
