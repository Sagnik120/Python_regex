# Python program to accept the strings
# which contains all the vowels



str = input()   #abcieaosyu
str = str.casefold()

vowels = set("aeiou")

s = set({})
	
for char in str:
    if char in vowels:  #
        s.add(char)
    else:
        pass			
	
if len(s) == len(vowels) :
	print("Accepted")
else :
	print("Not Accepted")



	
