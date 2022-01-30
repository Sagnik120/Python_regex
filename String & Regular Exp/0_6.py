#Count all letters, digits, and special symbols from a given string

sample_str = "sachin100hundreds@600matches"

char_count = 0
digit_count = 0
symbol_count = 0

for char in sample_str:
       if char.isalpha():
            char_count += 1
       elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
       else:
            symbol_count += 1
print("total counts of chars, Digits, and symbols \n")
print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)




