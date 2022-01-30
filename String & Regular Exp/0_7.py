#Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to VIT. vit No.1 private university in India"
sub_string = "VIT"

# convert string to lowercase
temp_str = str1.lower()
ss=sub_string.casefold()

# use count function
count = temp_str.count(ss)
print("The VIT count is:", count)




