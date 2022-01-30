# to remove duplicate words from a given string.

text_str = input() #sachin ramesh sachin
print("Original String:")

print(text_str)


l = text_str.split()
temp = []

for x in l:
    if x not in temp:
            temp.append(x)
print("\nAfter removing duplicate words from the said string:")
print(' '.join(temp))


