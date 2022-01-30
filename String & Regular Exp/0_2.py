# Program to check if a string
# is palindrome or not

# change this value for a different output
str = input()

# make it suitable for caseless comparison
str = str.casefold()

# reverse the string
rev_str = str[::-1]

# check if the string is equal to its reverse
if str == rev_str:
	print("palindrome")
else:
	print("not palindrome")
