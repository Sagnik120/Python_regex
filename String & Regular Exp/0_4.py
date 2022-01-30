#Check validity of PAN card number with string handling

pan=input("Enter Pan: ")
invalid = False
if len(pan)!=10:
    invalid = True
else:
    for i in range(0,5):
        if not pan[i].isalpha():
            invalid = True
            break
    for i in range(5,9):
        if not pan[i].isdigit():
            invalid = True
            break
if not pan[9].isalpha():
    invalid = True
if invalid == True:
    print("Invalid")
else:
    print("Given PAN %s is Valid" %(pan))
    
     


